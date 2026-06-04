#!/usr/bin/env python3
"""Assemble rewritten chunk files into one publishable Markdown file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROCESS_LABELS = (
    "改写说明",
    "洗稿说明",
    "质量检查",
    "结构分析",
    "相似风险",
    "生成策略",
)


def clean_chunk(text: str) -> str:
    lines = []
    for line in text.replace("\r\n", "\n").replace("\r", "\n").splitlines():
        stripped = line.strip()
        if any(stripped.startswith(label) for label in PROCESS_LABELS):
            continue
        if re.match(r"^[-*_]{3,}$", stripped):
            continue
        lines.append(line.rstrip())
    cleaned = "\n".join(lines).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def chunk_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"(\d+)", path.stem)
    return (int(match.group(1)) if match else 10**9, path.name)


def assemble(input_dir: Path, output_file: Path) -> None:
    files = sorted(input_dir.glob("*.md"), key=chunk_sort_key)
    if not files:
        raise SystemExit(f"No .md files found in {input_dir}")
    parts = [clean_chunk(path.read_text(encoding="utf-8")) for path in files]
    text = "\n\n".join(part for part in parts if part).strip() + "\n"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding="utf-8")
    print(f"Assembled {len(files)} chunks into {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path, help="Directory containing rewritten chunk .md files")
    parser.add_argument("output_file", type=Path, help="Final Markdown output file")
    args = parser.parse_args()
    assemble(args.input_dir, args.output_file)


if __name__ == "__main__":
    main()
