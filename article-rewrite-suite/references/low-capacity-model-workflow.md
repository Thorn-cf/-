# Low-Capacity Model Workflow

Use this workflow when a model struggles with long manuscripts, long prompts, or multi-step reasoning.

## Principle

Move deterministic work into scripts and keep model prompts short. The model should only do one cognitive task at a time:

1. Read one chunk.
2. Preserve that chunk's function.
3. Rewrite it into publishable prose.
4. Save the result.

Do not ask a weaker model to hold the whole article, the entire skill, and a long output plan in one prompt.

## Script-Assisted Setup

Run:

```bash
python3 article-rewrite-suite/scripts/prepare_rewrite_job.py input.md rewrite-job
```

The script creates:

- `chunks/`: source chunks small enough for weaker models.
- `prompts/`: one short prompt per chunk.
- `rewritten/`: destination folder for rewritten chunks.
- `structure-map-template.md`: compact structure map for humans or stronger models to fill.
- `stability-locks-template.md`: facts, terms, stance, and logic locks.
- `final-assembly-checklist.md`: final merge and quality checks.
- `manifest.json`: chunk order and metadata.

## Recommended Low-Model Sequence

1. Generate the rewrite job with the script.
2. Fill only the most important stability locks: names, dates, numbers, core claims, and terms.
3. Give the model `prompts/chunk-001-prompt.md`.
4. Save the output as `rewritten/chunk-001.md`.
5. Continue chunk by chunk.
6. Assemble with:

```bash
python3 article-rewrite-suite/scripts/assemble_rewrite.py rewrite-job/rewritten final.md
```

7. Run a final human or stronger-model pass only for continuity and duplicated transitions.

## Prompt Budget Rules

For weaker models:

- Keep each source chunk around 1,500-2,500 Chinese characters.
- Do not include all reference files in the prompt.
- Do not include long theory about rewriting.
- Use four hard rules only: preserve facts, preserve paragraph function, rebuild expression, output publishable正文 only.
- Ask for one chunk and one version at a time.

## Per-Chunk Prompt Shape

Use this shape:

```text
任务：深度改写下面这一段长文分块，输出可发布正文。

硬性要求：
1. 保留事实、人物、时间、数字、因果和观点。
2. 保留本分块的段落功能和论证顺序。
3. 重新组织表达，不做机械同义词替换。
4. 只输出正文，不要改写说明、质量检查或分析。

分块：
...
```

## Recovery When The Model Gets Stuck

- Reduce chunk size to 800-1,200 Chinese characters.
- Ask it to rewrite only 3-5 paragraphs.
- Remove all optional instructions.
- If it still fails, ask for "忠实润色版" first, then run a second pass for deeper reconstruction.
- Keep section headings unchanged, then rewrite body paragraphs separately.

## Final Merge Rules

After assembling chunks:

- Remove duplicate headings introduced at chunk boundaries.
- Smooth transitions between adjacent chunks.
- Check terminology consistency.
- Remove any accidental labels such as "以下是改写稿".
- Ensure the final file starts directly with the title or body.
