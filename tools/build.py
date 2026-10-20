#!/usr/bin/env python3
"""Build the offline dashboard from the repository's editable source files."""

import argparse
import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.3"


def file_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Resource path is outside the project: {relative}")
    return path


def pretty(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def inline(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def yaml_lines(value, depth=0):
    """Render this policy's JSON-compatible types as YAML without dependencies."""
    indent = "  " * depth
    if isinstance(value, dict):
        for key, item in value.items():
            label = json.dumps(str(key), ensure_ascii=False) + ":"
            if isinstance(item, (dict, list)) and item:
                yield indent + label
                yield from yaml_lines(item, depth + 1)
            else:
                yield indent + label + " " + json.dumps(item, ensure_ascii=False)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)) and item:
                yield indent + "-"
                yield from yaml_lines(item, depth + 1)
            else:
                yield indent + "- " + json.dumps(item, ensure_ascii=False)


def build():
    policy = json.loads(file_path("config/role_access_policy.json").read_text(encoding="utf-8"))
    data = json.loads(file_path("data/programme_data.json").read_text(encoding="utf-8"))
    resources = json.loads(file_path("src/embedded_resources.json").read_text(encoding="utf-8"))

    # Preserve the registry's scientific-review record. Changes to a source
    # require deliberate review and a matching checksum and byte count.
    for source in data["sources"]:
        content = file_path(source["path"]).read_bytes()
        if hashlib.sha256(content).hexdigest() != source["checksum"]:
            raise ValueError(f"Source checksum differs from registry: {source['path']}")
        if len(content) != source["file_size_bytes"]:
            raise ValueError(f"Source byte count differs from registry: {source['path']}")

    generated = {
        "config/role_access_policy.yaml": ("\n".join(yaml_lines(policy)) + "\n").encode("utf-8")
    }
    embedded = {}
    for relative, metadata in resources.items():
        content = generated.get(relative)
        if content is None:
            content = file_path(relative).read_bytes()
        embedded[relative] = {
            **metadata,
            "base64": base64.b64encode(content).decode("ascii"),
        }

    substitutions = {
        "{{EVIDENCE_HUB_STYLES}}": file_path("styles.css").read_text(encoding="utf-8"),
        "{{EVIDENCE_HUB_RESOURCES}}": "window.EMBEDDED_RESOURCES = " + inline(embedded) + ";",
        "{{EVIDENCE_HUB_POLICY}}": "window.ROLE_ACCESS_POLICY = " + inline(policy) + ";",
        "{{EVIDENCE_HUB_DATA}}": "window.EVIDENCE_HUB_DATA = " + inline(data) + ";",
        "{{EVIDENCE_HUB_APP}}": file_path("app.js").read_text(encoding="utf-8"),
    }
    html = file_path("src/index.template.html").read_text(encoding="utf-8")
    for token, replacement in substitutions.items():
        if html.count(token) != 1:
            raise ValueError(f"Expected exactly one template token: {token}")
        html = html.replace(token, replacement, 1)
    generated["index.html"] = html.encode("utf-8")

    all_files = {}
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in relative.parts):
            continue
        if relative.as_posix() == "manifest.json" or path.suffix == ".pyc":
            continue
        all_files[relative.as_posix()] = path.read_bytes()
    all_files.update(generated)
    manifest = {
        "package": "Programme Evidence Hub Demonstrator",
        "version": VERSION,
        "entry_point": "index.html",
        "disclaimer": "All programme details, scientific findings, and organisations are illustrative. No real company or programme data is included.",
        "files": [
            {"path": path, "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}
            for path, content in sorted(all_files.items())
        ],
    }
    generated["manifest.json"] = pretty(manifest).encode("utf-8")
    return generated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without changing them.")
    args = parser.parse_args()
    generated = build()
    if args.check:
        stale = [name for name, content in generated.items()
                 if not file_path(name).exists() or file_path(name).read_bytes() != content]
        if stale:
            parser.exit(1, "Regenerate these files with python3 tools/build.py: " + ", ".join(stale) + "\n")
        print("Dashboard, policy export, source checksums, and manifest are consistent.")
    else:
        for name, content in generated.items():
            file_path(name).write_bytes(content)
        print(f"Built Programme Evidence Hub v{VERSION}: index.html, policy export, and manifest.")


if __name__ == "__main__":
    main()
