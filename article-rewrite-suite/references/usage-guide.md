# Usage Guide

Use this guide when a user has installed the skill and needs onboarding, trigger examples, or a clear explanation of what the skill does.

## What This Skill Does

`article-rewrite-suite` helps with long-form article transformation while preserving structure and quality:

- 翻译：中译英、英译中、跨语言本土化翻译。
- 洗稿：保留原文结构和观点，重建表达，输出可发布新稿。
- 改写：润色、降重、增强逻辑、调整语气。
- 仿写：提取原文结构和风格，用于同主题或新主题创作。
- 多版本生成：同一篇原文生成多个不同表达策略的版本。
- 长文处理：支持分批处理长稿，并维护术语、事实和结构一致性。
- 低模型辅助：把长文拆成小任务包，让能力一般的模型也能分块稳定改写。

## How To Trigger It

Users can trigger the skill explicitly by writing `$article-rewrite-suite` in the prompt:

```text
使用 $article-rewrite-suite 帮我洗一下这篇稿子，保留结构，输出一篇可发布的新稿。
```

The skill should also trigger implicitly when the user asks for:

- 洗稿
- 改写
- 仿写
- 降重
- 润色
- 翻译成本土化稿件
- 生成多篇结构一致的新稿
- 保留结构但换一种表达
- 质量不低于原文

## Recommended Prompts

### Deep Rewrite

```text
使用 $article-rewrite-suite 深度改写这篇文章。要求保留原文结构和核心观点，但重新组织表达，输出可直接发布的正文，不要显示改写说明和质量检查。
```

### Multiple Versions

```text
使用 $article-rewrite-suite 基于这篇原文生成 3 个版本：一个忠实改写版，一个深度重构版，一个公众号风格版。三版都要保留原文结构。
```

### Style Imitation

```text
使用 $article-rewrite-suite 分析这篇文章的结构和风格，然后用同样的写法仿写一篇关于【主题】的新稿。
```

### Translation And Localization

```text
使用 $article-rewrite-suite 把这篇英文稿翻译并本土化成中文公众号文章，保留结构，语言自然，适合中文读者。
```

### Long Manuscript

```text
使用 $article-rewrite-suite 处理一篇长稿。我会分多次发送，请你维护结构、术语和观点一致性，每次只输出当前部分的可发布改写稿。
```

### Low-Capacity Model Or Stuck Generation

```text
使用 $article-rewrite-suite 的低模型工作流，把这篇长稿拆成小分块和短提示词，方便逐段洗稿。
```

If working from files, run:

```bash
python3 article-rewrite-suite/scripts/prepare_rewrite_job.py input.md rewrite-job
```

Then rewrite files in `rewrite-job/prompts/` one by one, save outputs into `rewrite-job/rewritten/`, and assemble:

```bash
python3 article-rewrite-suite/scripts/assemble_rewrite.py rewrite-job/rewritten final.md
```

## Default Delivery Behavior

For article generation tasks, output only publication-ready article content by default:

- Do not include "改写说明".
- Do not include "质量检查".
- Do not include "结构分析".
- Do not explain the internal workflow unless the user asks.
- Start directly with the title or body.

If the user wants process notes, they can ask:

```text
请同时给我结构分析和质量检查。
```

## Best Inputs

For best results, ask users to provide:

- 原文全文或分批原文。
- 目标：洗稿、改写、仿写、翻译、本土化、多版本。
- 目标平台：公众号、小红书、知乎、新闻稿、博客、邮件等。
- 目标长度：等长、缩短、扩写、指定字数。
- 风格要求：克制、犀利、故事化、理性分析、口语化、专业化。
- 是否需要多版本。

## Example First Response After Installation

```text
你可以这样触发我：

使用 $article-rewrite-suite 帮我洗一下这篇稿子，保留结构和观点，输出一篇可发布的新稿。

我能做的事包括：翻译、洗稿、深度改写、仿写、多版本生成、长文分批处理和平台化改写。默认情况下，我会只输出可发布正文，不显示改写说明或质量检查；如果你想看结构分析和检查结果，可以单独要求。

如果模型处理长文时卡住，可以让我启用低模型工作流：我会先把长文拆成小分块和短提示词，再逐段生成，最后合并成完整稿。
```
