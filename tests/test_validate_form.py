import importlib.util
import re
import sys
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).parents[1]
MODULE_PATH = REPOSITORY / "scripts" / "validate_form.py"
SPEC = importlib.util.spec_from_file_location("validate_form", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


VALID_NATIVE = """<!doctype html>
<html>
  <head>
    <meta type="xrm/designer/setting" name="type"
          value="marketing-designer-content-editor-document">
  </head>
  <body>
    <form class="marketingForm" aria-label="Contact request">
      <div data-layout="true">
        <div data-section="true">
          <div data-container="true" data-container-width="100">
            <div data-editorblocktype="TextFormField"
                 data-targetproperty="emailaddress1"
                 data-required="required">
              <label for="email">Email</label>
              <input id="email" name="emailaddress1" type="email" required>
            </div>
          </div>
        </div>
        <div data-section="true">
          <div data-container="true" data-container-width="50">
            <div data-editorblocktype="Captcha"></div>
          </div>
          <div data-container="true" data-container-width="50">
            <div data-editorblocktype="SubmitButton">
              <button type="submit">Send</button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </body>
</html>
"""


INVALID_NATIVE = """<html><body>
<form class="marketingForm" onclick="submitNow()">
  <div data-editorblocktype="Consent" data-purposeid="undefined"
       data-channels="Email">
    <input id="same" name="undefined">
  </div>
  <input id="same" name="emailaddress1">
</form>
</body></html>
"""


VALID_CAPTURE = """<!doctype html>
<html><body>
<form id="existing-form">
  <label for="first">First name</label>
  <input id="first" name="firstName">
  <button type="submit">Send</button>
</form>
<script src="https://assets.example.microsoft/FormCapture.bundle.js"></script>
<script>
d365mktformcapture.waitForElement("#existing-form").then((form) => {
  const mappings = [
    { FormFieldName: "firstName", DataverseFieldName: "firstname" }
  ];
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const serialized = d365mktformcapture.serializeForm(form, mappings);
    const payload = serialized.SerializedForm.build();
    const captureConfig = {
      FormId: "8bb6ecb1-42f3-4aac-8af4-111111111111",
      FormApiUrl: "https://example.dynamics.com/api/v1.0/forms"
    };
    d365mktformcapture.submitForm(captureConfig, payload).then(() => {});
  });
});
</script>
</body></html>
"""


INVALID_CAPTURE = """<html><body>
<form id="existing"><input name="email"><button type="submit">Send</button></form>
<script src="FormCapture.bundle.js"></script>
<script>
d365mktformcapture.waitForElement("#existing").then((form) => {
  const mappings = [{ FormFieldName: "missing", DataverseFieldName: "emailaddress1" }];
  const payload = d365mktformcapture.serializeForm(form, mappings).SerializedForm.build();
  d365mktformcapture.submitForm({FormId: "...", FormApiUrl: "***Please fill***"}, payload);
});
</script>
</body></html>
"""


class ValidateFormTests(unittest.TestCase):
    def codes(self, source: str, mode: str) -> tuple[list[str], list[str]]:
        resolved, findings = VALIDATOR.validate_text(source, mode)
        self.assertEqual(resolved, mode)
        errors = [item.code for item in findings if item.severity == "error"]
        warnings = [item.code for item in findings if item.severity == "warning"]
        return errors, warnings

    def test_valid_native_has_no_errors(self) -> None:
        errors, _ = self.codes(VALID_NATIVE, "native")
        self.assertEqual(errors, [])

    def test_invalid_native_reports_structural_and_placeholder_errors(self) -> None:
        errors, warnings = self.codes(INVALID_NATIVE, "native")
        self.assertIn("duplicate-id", errors)
        self.assertIn("placeholder-value", errors)
        self.assertIn("submit", errors)
        self.assertIn("inline-event", warnings)

    def test_valid_capture_has_no_errors(self) -> None:
        errors, _ = self.codes(VALID_CAPTURE, "capture")
        self.assertEqual(errors, [])

    def test_invalid_capture_reports_environment_and_mapping_errors(self) -> None:
        errors, warnings = self.codes(INVALID_CAPTURE, "capture")
        self.assertIn("capture-form-id", errors)
        self.assertIn("capture-api-url", errors)
        self.assertIn("capture-control", errors)
        self.assertIn("capture-promise", warnings)

    def test_auto_detects_capture(self) -> None:
        mode, _ = VALIDATOR.validate_text(VALID_CAPTURE, "auto")
        self.assertEqual(mode, "capture")

    def test_json_option_metadata_is_not_a_placeholder(self) -> None:
        self.assertFalse(
            VALIDATOR.is_placeholder('[{"value":"1","label":"Option 1"}]')
        )

    def test_button_without_type_is_a_submit_control(self) -> None:
        button = VALIDATOR.Node("button", {}, None, 1)
        self.assertTrue(VALIDATOR.is_submit_control(button))

    def test_repository_smoke_form_has_no_structural_errors(self) -> None:
        source = (REPOSITORY / "test.html").read_text(encoding="utf-8")
        errors, _ = self.codes(source, "native")
        self.assertEqual(errors, [])

    def test_archival_lead_export_is_rejected_as_deployable(self) -> None:
        source = (REPOSITORY / "examples/lead/default.html").read_text(
            encoding="utf-8"
        )
        errors, _ = self.codes(source, "native")
        self.assertIn("consent-config", errors)
        self.assertIn("placeholder-value", errors)


class SkillDocumentationTests(unittest.TestCase):
    def test_local_markdown_links_exist(self) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        documents = [
            REPOSITORY / "SKILL.md",
            REPOSITORY / "README.md",
            *sorted((REPOSITORY / "references").glob("*.md")),
        ]
        for document in documents:
            source = document.read_text(encoding="utf-8")
            for raw_target in link_pattern.findall(source):
                if raw_target.startswith(("http://", "https://", "#")):
                    continue
                target = raw_target.split("#", 1)[0]
                with self.subTest(document=document.name, target=target):
                    self.assertTrue((document.parent / target).is_file())


if __name__ == "__main__":
    unittest.main()
