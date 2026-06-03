---
name: article-rewrite-suite
description: Translate, rewrite, polish, localize, or imitate long-form manuscripts while preserving the original article structure and producing one or more high-quality new drafts. Use when the user provides or references a 2,000- to very-long-form article and asks for 翻译, 洗稿, 改写, 仿写, 扩写, 缩写, 本土化, 多版本产出, 保留结构, 保持观点, or generating publishable derivative drafts whose quality must not be lower than the source.
---

# Article Rewrite Suite

## Core Rule

Treat the source manuscript as a structure and argument blueprint, not as text to mechanically replace. Preserve the article's section order, paragraph function, argument flow, examples' roles, emotional rhythm, and conclusion intent unless the user explicitly asks to change them.

Always produce original expression. Do not copy distinctive sentences, unusual metaphors, proprietary phrasing, or long verbatim passages from the source unless the user asks for quotation and the quote is necessary.

Default to a three-stage system: distill the structure, rebuild the expression, then run quality and similarity-risk checks. For "洗稿" and "仿写", work from the distilled outline and paragraph functions instead of rewriting sentence by sentence.

## Intake

Before writing, identify:

- Source language, target language, approximate length, and whether the text is complete.
- User goal: translation, faithful rewrite, deep rewrite, imitation, localization, expansion, compression, polishing, or multiple versions.
- Required number of drafts, target length, audience, tone, platform, and any forbidden changes.
- Structure map: title, headings, major claims, evidence, examples, transitions, and conclusion.

If critical choices are missing, make conservative defaults and state them briefly: preserve structure, keep length within about 10 percent of the source, generate one polished version, and avoid adding unsupported facts.

## Workflow

1. **Structure distillation**: create a structure map before drafting. Capture title intent, heading hierarchy, section purpose, paragraph functions, key claims, examples, transitions, emotional curve, and conclusion move.
2. **Stability locks**: extract fact locks, term locks, stance locks, and style fingerprint. These are the guardrails for every version.
3. **Mode selection**: use the user's requested operation. If the request says "多种方式", create distinct modes such as faithful translation, deep rewrite, style imitation, localized adaptation, compression, or expansion.
4. **Expression rebuild**: rewrite from the distilled structure and paragraph functions. Do not keep sentence order unless required by translation. Change openings, transitions, rhetorical devices, and paragraph rhythm while preserving meaning.
5. **Version differentiation**: for multiple drafts, assign each version a different rewrite strategy, such as faithful polish, deep reconstruction, platform optimization, story-driven expression, rational analysis, or concise edition.
6. **Quality and risk gate**: compare each draft against the structure map, stability locks, quality rubric, and similarity-risk scan. Repair failed sections before final delivery.

## Output Format

For normal rewrite, washing, imitation, polishing, or translation requests, output only publication-ready article content by default:

- Start directly with the rewritten title or body.
- Preserve the same heading hierarchy as the source when applicable.
- Do not include process labels such as "改写说明", "洗稿说明", "质量检查", "相似风险", "结构分析", or "生成策略".
- Do not append commentary before or after the draft unless the user explicitly asks for analysis, comparison, checklist, or explanation.
- Keep quality checks, structure maps, stability locks, and similarity-risk scans internal.

When generating multiple versions, label only the version names needed for selection, such as "版本一", "版本二", or user-specified names. Avoid exposing the underlying rewrite mechanics unless requested.

For very long manuscripts, avoid flooding the user with a whole book-length answer at once. Offer a batch plan, then process in chunks while maintaining a shared outline and version log.

## Mode Selection

Use [references/modes.md](references/modes.md) when choosing or explaining rewrite modes.

Use [references/rewriting-methods.md](references/rewriting-methods.md) for structure distillation, paragraph-function rewriting, fact locks, style fingerprints, multi-version differentiation, similarity-risk scanning, and repair loops.

Use [references/long-form-workflow.md](references/long-form-workflow.md) when the source is long, multi-chapter, pasted in batches, or likely to exceed a single response.

Use [references/quality-rubric.md](references/quality-rubric.md) for final checks, especially when the user requires "质量不低于原文", "可发布", "多篇", or "结构不变".

## Guardrails

- Do not invent factual details to make the draft feel richer. Mark optional enhancement ideas separately when helpful.
- Do not reduce quality by flattening voice, deleting nuance, or replacing strong examples with generic ones.
- Do not over-preserve sentence order if it causes copied phrasing; preserve paragraph and section function instead.
- Do not claim a draft is legally safe or plagiarism-proof. Say it is more original and structurally faithful, then suggest human/legal review for high-stakes publishing.
- If the manuscript contains copyrighted or private content, transform it according to the user's rights and intent, but avoid reproducing large source passages verbatim.
