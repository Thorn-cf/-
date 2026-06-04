#!/usr/bin/env python3
"""Create a low-prompt rewrite job from a long Markdown manuscript."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def split_blocks(text: str) -> list[str]:
    parts = re.split(r"\n{2,}", text.strip())
    return [part.strip() for part in parts if part.strip()]


def block_size(block: str) -> int:
    return len(block)


def split_oversized_block(block: str, limit: int) -> list[str]:
    if len(block) <= limit:
        return [block]
    sentences = re.split(r"(?<=[。！？!?；;])", block)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if current and len(current) + len(sentence) > limit:
            chunks.append(current.strip())
            current = sentence
        else:
            current = f"{current}{sentence}"
    if current.strip():
        chunks.append(current.strip())
    return chunks or [block]


def make_chunks(text: str, limit: int) -> list[str]:
    blocks: list[str] = []
    for block in split_blocks(text):
        blocks.extend(split_oversized_block(block, limit))

    chunks: list[str] = []
    current: list[str] = []
    current_size = 0
    for block in blocks:
        size = block_size(block)
        is_heading = block.lstrip().startswith("#")
        if current and (current_size + size > limit or is_heading):
            chunks.append("\n\n".join(current).strip())
            current = [block]
            current_size = size
        else:
            current.append(block)
            current_size += size
    if current:
        chunks.append("\n\n".join(current).strip())
    return chunks


def extract_headings(text: str) -> list[dict[str, str | int]]:
    headings = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append({"level": len(match.group(1)), "title": match.group(2)})
    return headings


def prompt_for_chunk(index: int, total: int, chunk: str, mode: str) -> str:
    return f"""任务：按“{mode}”模式改写下面的长文分块，输出可发布正文。

分块位置：{index}/{total}

硬性要求：
1. 保留人物、时间、数字、地点、因果、观点和段落功能。
2. 保留本分块内部的论证顺序；不要新增未经原文支持的事实。
3. 重新组织表达、段首、衔接和句式，避免机械同义词替换。
4. 只输出正文；不要输出改写说明、质量检查、结构分析或过程解释。

当前分块：

{chunk}
"""


def write_job(input_path: Path, output_dir: Path, limit: int, mode: str) -> None:
    text = read_text(input_path)
    chunks = make_chunks(text, limit)
    headings = extract_headings(text)

    chunks_dir = output_dir / "chunks"
    prompts_dir = output_dir / "prompts"
    rewritten_dir = output_dir / "rewritten"
    for directory in (chunks_dir, prompts_dir, rewritten_dir):
        directory.mkdir(parents=True, exist_ok=True)

    manifest = {
        "source": str(input_path),
        "chunk_char_limit": limit,
        "mode": mode,
        "chunk_count": len(chunks),
        "chunks": [],
        "headings": headings,
    }

    for idx, chunk in enumerate(chunks, start=1):
        name = f"chunk-{idx:03d}.md"
        prompt_name = f"chunk-{idx:03d}-prompt.md"
        (chunks_dir / name).write_text(chunk + "\n", encoding="utf-8")
        (prompts_dir / prompt_name).write_text(
            prompt_for_chunk(idx, len(chunks), chunk, mode), encoding="utf-8"
        )
        manifest["chunks"].append(
            {
                "index": idx,
                "source": f"chunks/{name}",
                "prompt": f"prompts/{prompt_name}",
                "rewrite_target": f"rewritten/{name}",
                "chars": len(chunk),
            }
        )

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    heading_lines = "\n".join(
        f"{'#' * int(item['level'])} {item['title']}" for item in headings
    )
    (output_dir / "structure-map-template.md").write_text(
        f"""# Structure Map

## Source Headings

{heading_lines or "No Markdown headings detected."}

## Fill Before Rewriting

- Title intent:
- Central thesis:
- Audience:
- Tone:
- Section purposes:
- Emotional curve:
- Conclusion move:
""",
        encoding="utf-8",
    )

    (output_dir / "stability-locks-template.md").write_text(
        """# Stability Locks

Fill only the facts that must not drift.

## Fact Locks

- Names:
- Dates:
- Numbers:
- Places:
- Definitions:

## Logic Locks

- Cause and effect:
- Chronology:
- Comparisons:

## Stance Locks

- Author attitude:
- Recommendation:
- Uncertainty level:

## Term Locks

- Required terms:
- Required translations:
""",
        encoding="utf-8",
    )

    (output_dir / "final-assembly-checklist.md").write_text(
        """# Final Assembly Checklist

- Assemble rewritten chunks in manifest order.
- Remove duplicate headings or repeated transitions at chunk boundaries.
- Keep final output publication-ready: no rewrite notes, quality checks, or process labels.
- Check names, dates, numbers, terms, and causality against stability locks.
- Smooth section transitions after assembly.
- Confirm the final file starts directly with the title or body.
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source Markdown/text file")
    parser.add_argument("output_dir", type=Path, help="Directory for rewrite job files")
    parser.add_argument("--chunk-chars", type=int, default=2200)
    parser.add_argument("--mode", default="深度改写/洗稿")
    args = parser.parse_args()

    if args.chunk_chars < 500:
        raise SystemExit("--chunk-chars must be at least 500")
    write_job(args.input, args.output_dir, args.chunk_chars, args.mode)
    print(f"Created rewrite job at {args.output_dir}")


if __name__ == "__main__":
    main()
