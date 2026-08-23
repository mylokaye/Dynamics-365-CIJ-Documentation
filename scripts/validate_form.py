#!/usr/bin/env python3
"""Local preflight checks for Customer Insights form source and Form Capture pages.

This checker deliberately does not claim platform compatibility. Customer Insights
must still save, validate, publish, and process a unique test submission.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}
CONTROL_TAGS = {"input", "select", "textarea", "button"}
PLACEHOLDER_MARKERS = (
    "***please fill***",
    "your-image-url-here",
    "your-form-id",
    "your-api-url",
    "generated_id",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    line: int | None = None


@dataclass
class Node:
    tag: str
    attrs: dict[str, str]
    parent: int | None
    line: int


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.nodes: list[Node] = []
        self.stack: list[int] = []
        self.has_doctype = False

    def handle_decl(self, decl: str) -> None:
        if decl.lower().startswith("doctype"):
            self.has_doctype = True

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._add_node(tag, attrs, push=tag.lower() not in VOID_TAGS)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._add_node(tag, attrs, push=False)

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.lower()
        for position in range(len(self.stack) - 1, -1, -1):
            if self.nodes[self.stack[position]].tag == lowered:
                del self.stack[position:]
                return

    def _add_node(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
        *,
        push: bool,
    ) -> None:
        normalized = {key.lower(): value or "" for key, value in attrs}
        parent = self.stack[-1] if self.stack else None
        node = Node(tag.lower(), normalized, parent, self.getpos()[0])
        self.nodes.append(node)
        if push:
            self.stack.append(len(self.nodes) - 1)


def ancestors(inspector: Inspector, index: int) -> Iterable[int]:
    parent = inspector.nodes[index].parent
    while parent is not None:
        yield parent
        parent = inspector.nodes[parent].parent


def is_descendant(inspector: Inspector, index: int, ancestor: int) -> bool:
    return ancestor in ancestors(inspector, index)


def descendants(inspector: Inspector, index: int) -> list[tuple[int, Node]]:
    return [
        (candidate, node)
        for candidate, node in enumerate(inspector.nodes)
        if is_descendant(inspector, candidate, index)
    ]


def class_names(node: Node) -> set[str]:
    return set(node.attrs.get("class", "").split())


def is_submit_control(node: Node) -> bool:
    control_type = node.attrs.get("type", "").lower()
    if node.tag == "button":
        return control_type in {"", "submit"}
    return node.tag == "input" and control_type in {"submit", "image"}


def is_placeholder(value: str) -> bool:
    lowered = value.strip().lower()
    return (
        lowered in {"undefined", "null", "...", "todo", "tbd"}
        or "please fill" in lowered
        or any(marker in lowered for marker in PLACEHOLDER_MARKERS)
        or bool(re.search(r"\{[A-Za-z][A-Za-z0-9_.-]*\}", value))
    )


def common_findings(inspector: Inspector, source: str) -> list[Finding]:
    findings: list[Finding] = []
    ids: dict[str, list[int]] = {}
    control_ids: set[str] = set()

    for node in inspector.nodes:
        node_id = node.attrs.get("id")
        if node_id:
            ids.setdefault(node_id, []).append(node.line)
            if node.tag in CONTROL_TAGS:
                control_ids.add(node_id)

        for attribute in node.attrs:
            if attribute.startswith("on"):
                findings.append(
                    Finding(
                        "warning",
                        "inline-event",
                        f"Inline event attribute {attribute!r} can be sanitized; use addEventListener.",
                        node.line,
                    )
                )

        for attribute, value in node.attrs.items():
            critical = (
                attribute.startswith("data-")
                or attribute in {"name", "value", "action", "src"}
            )
            if critical and is_placeholder(value):
                findings.append(
                    Finding(
                        "error",
                        "placeholder-value",
                        f"Replace non-deployable {attribute}={value!r} with a target-environment value.",
                        node.line,
                    )
                )

    for node_id, lines in ids.items():
        if len(lines) > 1:
            findings.append(
                Finding(
                    "error",
                    "duplicate-id",
                    f"ID {node_id!r} occurs {len(lines)} times.",
                    lines[0],
                )
            )

    for node in inspector.nodes:
        if node.tag == "label" and node.attrs.get("for"):
            target = node.attrs["for"]
            if target not in control_ids:
                findings.append(
                    Finding(
                        "warning",
                        "label-target",
                        f"Label target {target!r} does not match a control ID.",
                        node.line,
                    )
                )

    lowered_source = source.lower()
    for marker in PLACEHOLDER_MARKERS:
        if marker in lowered_source:
            findings.append(
                Finding(
                    "error",
                    "placeholder-marker",
                    f"Unresolved placeholder marker {marker!r} remains in the document.",
                )
            )

    return findings


def validate_native(inspector: Inspector, source: str) -> list[Finding]:
    findings = common_findings(inspector, source)
    forms = [
        index
        for index, node in enumerate(inspector.nodes)
        if node.tag == "form" and "marketingForm" in class_names(node)
    ]
    if len(forms) != 1:
        findings.append(
            Finding(
                "error",
                "marketing-form-count",
                f"Expected exactly one form.marketingForm; found {len(forms)}.",
            )
        )
        return findings

    form_index = forms[0]
    form = inspector.nodes[form_index]
    form_nodes = descendants(inspector, form_index)
    controls = [(index, node) for index, node in form_nodes if node.tag in CONTROL_TAGS]
    submit_controls = [node for _, node in controls if is_submit_control(node)]
    if not submit_controls:
        findings.append(
            Finding("error", "submit", "The marketing form has no submit control.", form.line)
        )

    if not form.attrs.get("aria-label") and not form.attrs.get("aria-labelledby"):
        findings.append(
            Finding(
                "warning",
                "form-name",
                "Give the marketing form an accessible name.",
                form.line,
            )
        )

    layout_nodes = [
        index
        for index, node in form_nodes
        if node.attrs.get("data-layout", "").lower() == "true"
    ]
    if not layout_nodes:
        findings.append(
            Finding(
                "warning",
                "designer-layout",
                "No data-layout region found. Full-page HTML can render, but drag-and-drop layout support may be limited.",
                form.line,
            )
        )

    sections = [
        index
        for index, node in form_nodes
        if node.attrs.get("data-section", "").lower() == "true"
    ]
    containers = [
        index
        for index, node in form_nodes
        if node.attrs.get("data-container", "").lower() == "true"
    ]

    for section_index in sections:
        section = inspector.nodes[section_index]
        if layout_nodes and not any(
            is_descendant(inspector, section_index, layout) for layout in layout_nodes
        ):
            findings.append(
                Finding(
                    "error",
                    "section-parent",
                    "A data-section region is not inside data-layout.",
                    section.line,
                )
            )
        direct_containers = [
            inspector.nodes[index]
            for index in containers
            if inspector.nodes[index].parent == section_index
        ]
        if not direct_containers:
            findings.append(
                Finding(
                    "warning",
                    "empty-section",
                    "A data-section region has no direct data-container child.",
                    section.line,
                )
            )
            continue
        widths: list[float] = []
        for container in direct_containers:
            raw_width = container.attrs.get("data-container-width")
            if raw_width:
                try:
                    widths.append(float(raw_width))
                except ValueError:
                    findings.append(
                        Finding(
                            "error",
                            "container-width",
                            f"Invalid data-container-width value {raw_width!r}.",
                            container.line,
                        )
                    )
        if widths and abs(sum(widths) - 100.0) > 0.1:
            findings.append(
                Finding(
                    "warning",
                    "container-width-total",
                    f"Direct container widths total {sum(widths):g}, not 100.",
                    section.line,
                )
            )

    mapped_blocks = [
        (index, node)
        for index, node in form_nodes
        if node.attrs.get("data-targetproperty")
    ]
    if not mapped_blocks:
        findings.append(
            Finding(
                "warning",
                "mapped-fields",
                "No mapped field blocks found. Confirm fields through the target form editor.",
                form.line,
            )
        )

    for block_index, block in mapped_blocks:
        target = block.attrs["data-targetproperty"]
        block_controls = [
            node
            for _, node in descendants(inspector, block_index)
            if node.tag in {"input", "select", "textarea"}
        ]
        if not block_controls:
            findings.append(
                Finding(
                    "error",
                    "mapped-control",
                    f"Mapped block {target!r} contains no native control.",
                    block.line,
                )
            )
            continue
        if not any(control.attrs.get("name") == target for control in block_controls):
            findings.append(
                Finding(
                    "warning",
                    "mapped-name",
                    f"Mapped block {target!r} has no descendant control with the same name.",
                    block.line,
                )
            )

        block_required = block.attrs.get("data-required", "").lower() in {
            "required",
            "true",
        }
        native_required = any("required" in control.attrs for control in block_controls)
        if block_required != native_required:
            findings.append(
                Finding(
                    "warning",
                    "required-mismatch",
                    f"Mapped block {target!r} has inconsistent Designer and native required markers.",
                    block.line,
                )
            )

    for control_index, control in controls:
        if is_submit_control(control) or control.attrs.get("type", "").lower() in {
            "button",
            "reset",
        }:
            continue
        if any(
            inspector.nodes[parent].attrs.get("data-editorblocktype")
            for parent in ancestors(inspector, control_index)
            if is_descendant(inspector, parent, form_index) or parent == form_index
        ):
            continue
        findings.append(
            Finding(
                "warning",
                "unmanaged-control",
                f"Control {control.attrs.get('name') or control.tag!r} is not inside a Designer block and may not be processed.",
                control.line,
            )
        )

    consent_blocks = [
        node
        for _, node in form_nodes
        if node.attrs.get("data-editorblocktype", "").lower() in {"consent", "topic"}
    ]
    for block in consent_blocks:
        block_type = block.attrs.get("data-editorblocktype", "").lower()
        required_attrs = ["data-purposeid", "data-channels"]
        if block_type == "topic":
            required_attrs.append("data-topicid")
        for attribute in required_attrs:
            value = block.attrs.get(attribute, "")
            if not value or is_placeholder(value):
                findings.append(
                    Finding(
                        "error",
                        "consent-config",
                        f"{block_type.title()} block needs a target-environment {attribute} value.",
                        block.line,
                    )
                )

    has_captcha = any(
        node.attrs.get("data-editorblocktype", "").lower() in {"captcha", "recaptcha"}
        for _, node in form_nodes
    )
    if not has_captcha:
        findings.append(
            Finding(
                "warning",
                "recaptcha",
                "No reCAPTCHA Designer block was found. Add one before publishing a public form.",
                form.line,
            )
        )

    has_designer_meta = any(
        node.tag == "meta"
        and node.attrs.get("type") == "xrm/designer/setting"
        and node.attrs.get("name") == "type"
        and node.attrs.get("value") == "marketing-designer-content-editor-document"
        for node in inspector.nodes
    )
    if not has_designer_meta:
        findings.append(
            Finding(
                "warning",
                "designer-meta",
                "Designer drag-and-drop meta tag not found; the simplified full-page editor may be used.",
            )
        )

    for index, node in enumerate(inspector.nodes):
        if node.tag == "script" and any(
            inspector.nodes[parent].tag == "head" for parent in ancestors(inspector, index)
        ):
            findings.append(
                Finding(
                    "warning",
                    "head-script",
                    "Current versions move head scripts to the body; verify the saved target-environment source.",
                    node.line,
                )
            )

    return findings


def validate_capture(inspector: Inspector, source: str) -> list[Finding]:
    findings = common_findings(inspector, source)
    lowered = source.lower()
    forms = [node for node in inspector.nodes if node.tag == "form"]
    if not forms:
        findings.append(Finding("error", "capture-form", "No existing form element found."))
    if not any(is_submit_control(node) for node in inspector.nodes):
        findings.append(Finding("error", "submit", "The captured page has no submit control."))

    required_tokens = {
        "FormCapture.bundle.js": "formcapture.bundle.js",
        "waitForElement": "d365mktformcapture.waitforelement",
        "serializeForm": "d365mktformcapture.serializeform",
        "submitForm": "d365mktformcapture.submitform",
    }
    for label, token in required_tokens.items():
        if token not in lowered:
            findings.append(
                Finding(
                    "error",
                    "capture-api",
                    f"Generated Form Capture integration is missing {label}.",
                )
            )

    form_ids = re.findall(r"\bFormId\s*:\s*['\"]([^'\"]+)['\"]", source)
    api_urls = re.findall(r"\bFormApiUrl\s*:\s*['\"]([^'\"]+)['\"]", source)
    if not form_ids or any(is_placeholder(value) for value in form_ids):
        findings.append(
            Finding(
                "error",
                "capture-form-id",
                "Use the FormId from the generated target-environment capture snippet.",
            )
        )
    if not api_urls or any(is_placeholder(value) for value in api_urls):
        findings.append(
            Finding(
                "error",
                "capture-api-url",
                "Use the FormApiUrl from the generated target-environment capture snippet.",
            )
        )

    mapping_names = re.findall(
        r"\bFormFieldName\s*:\s*['\"]([^'\"]+)['\"]", source
    )
    if not mapping_names:
        findings.append(
            Finding("error", "capture-mappings", "No FormFieldName mappings found.")
        )
    control_names = {
        node.attrs["name"]
        for node in inspector.nodes
        if node.tag in {"input", "select", "textarea"} and node.attrs.get("name")
    }
    for name in mapping_names:
        if name not in control_names:
            findings.append(
                Finding(
                    "error",
                    "capture-control",
                    f"FormFieldName {name!r} does not match an existing control name.",
                )
            )

    dataverse_names = re.findall(
        r"\bDataverseFieldName\s*:\s*['\"]([^'\"]+)['\"]", source
    )
    if mapping_names and len(dataverse_names) < len(mapping_names):
        findings.append(
            Finding(
                "warning",
                "capture-dataverse-mapping",
                "Some form-field mappings do not include a DataverseFieldName; verify generated value mappings and unmapped fields.",
            )
        )

    if "preventdefault(" not in lowered:
        findings.append(
            Finding(
                "warning",
                "submission-ownership",
                "No preventDefault call found. Confirm whether original or dual submission is intentional.",
            )
        )
    if "await d365mktformcapture.submitform" not in lowered and not re.search(
        r"d365mktformcapture\.submitForm\s*\([^;]+\)\s*\.(then|catch)",
        source,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        findings.append(
            Finding(
                "warning",
                "capture-promise",
                "Handle the submitForm promise before redirecting or showing success.",
            )
        )
    if "window.location" in lowered or "location.href" in lowered:
        findings.append(
            Finding(
                "warning",
                "capture-redirect",
                "Verify that navigation occurs only after submitForm and any required original destination complete.",
            )
        )

    return findings


def validate_text(source: str, mode: str = "auto") -> tuple[str, list[Finding]]:
    inspector = Inspector()
    inspector.feed(source)
    inspector.close()
    resolved_mode = mode
    if mode == "auto":
        lowered = source.lower()
        resolved_mode = (
            "capture"
            if "d365mktformcapture" in lowered or "formcapture.bundle.js" in lowered
            else "native"
        )
    if resolved_mode == "capture":
        return resolved_mode, validate_capture(inspector, source)
    return resolved_mode, validate_native(inspector, source)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run local preflight checks on a native Customer Insights form or Form Capture page."
    )
    parser.add_argument("path", type=Path, help="HTML file to inspect")
    parser.add_argument(
        "--mode", choices=("auto", "native", "capture"), default="auto"
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument(
        "--strict", action="store_true", help="Return nonzero when warnings exist"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.path.is_file():
        print(f"ERROR file: {args.path} does not exist or is not a file.", file=sys.stderr)
        return 2

    source = args.path.read_text(encoding="utf-8")
    mode, findings = validate_text(source, args.mode)
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
    payload = {
        "file": str(args.path),
        "mode": mode,
        "findings": [asdict(item) for item in findings],
        "summary": {"errors": errors, "warnings": warnings},
        "scope": (
            "Local preflight only. Customer Insights must still save, pass Check content, "
            "publish, and process a verified test submission."
        ),
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for item in findings:
            location = f" line {item.line}" if item.line else ""
            print(f"{item.severity.upper()} {item.code}{location}: {item.message}")
        print(
            f"SUMMARY mode={mode} errors={errors} warnings={warnings} file={args.path}"
        )
        print(f"NOTE {payload['scope']}")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
