import { mkdir, readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";

const projectRoot = resolve(new URL("..", import.meta.url).pathname);
const source = await readFile(resolve(projectRoot, "test.html"), "utf8");
const output = resolve(projectRoot, "dist/server/index.js");

await mkdir(resolve(projectRoot, "dist/server"), { recursive: true });

const worker = `const HTML = ${JSON.stringify(source)};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (url.pathname === "/" || url.pathname === "/index.html" || url.pathname === "/test.html") {
      return new Response(HTML, {
        headers: { "content-type": "text/html; charset=utf-8" }
      });
    }
    return new Response("Not found", { status: 404 });
  }
};
`;

await writeFile(output, worker, "utf8");
console.log(`Built ${output}`);
