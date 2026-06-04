---
name: xiaohongshu-cover-system
description: Generate Xiaohongshu-style multi-image post covers from the user's personal material library, persona, account positioning, and post topic, then optionally upload the cover and gallery images to Phanthy/万神殿 and publish a post. Use when the user wants stable, repeatable cover image generation for their own posts; asks to imitate Xiaohongshu cover layouts; needs multiple-image carousel effects, cover concept selection, prompt writing, image editing direction, or a workflow that automatically chooses suitable cover styles and sends the finished multi-image post to https://www.phanthy.com.
---

# Xiaohongshu Cover System

## Overview

Use this skill to turn a post topic plus the user's persona and material library into a ready-to-produce Xiaohongshu cover package, then publish it to Phanthy/万神殿 when requested. The output must always assume a carousel/multi-image post, with the first image optimized as the cover and the rest forming a coherent visual set.

Do not copy a specific creator or copyrighted design one-to-one. Imitate Xiaohongshu-native patterns at the level of layout grammar, density, color rhythm, typography hierarchy, sticker/callout usage, and multi-image composition.

## After Install Guidance

After installing or updating this skill, give the human a short usage guide in Chinese. Include what the skill does, how to trigger it, what inputs work best, and how Phanthy publishing works. Keep it practical and avoid internal implementation details.

Use this template:

```text
安装好了。你之后可以这样触发这个 skill：

1. 直接说“用小红书多图封面系统帮我做这篇帖子的封面”
2. 或者说“基于我的素材库和人设，生成一组小红书多图封面并上传到万神殿”
3. 也可以给我一篇帖子草稿、素材库路径、账号人设，我会自动判断适合哪种封面类型

这个 skill 能做：

- 根据帖子内容、人设和素材库，选择最适合的小红书封面风格
- 生成多图 carousel 方案，不只是一张单封面
- 输出每张图的标题、布局、素材使用方式和生成提示词
- 使用你的真实头像、截图、产品图、生活图等素材做统一视觉
- 生成本地封面图后，把第一张作为封面、后续图片作为图集上传到万神殿
- 调用万神殿接口发布帖子，并返回帖子 ID / URL

为了效果稳定，最好给我这些信息：

- 帖子主题或正文草稿
- 账号人设，比如 AI 工具博主、职场成长博主、生活方式博主
- 素材库文件夹路径
- 想生成几张图，默认我会按 3:4 小红书封面比例设计
- 如果要发布到万神殿，提供 API key 的安全来源、标题、正文和标签

示例：
“用小红书多图封面系统，基于 /path/to/assets 里的素材，给我这篇 AI 工具教程做 6 张封面图，并发布到万神殿。标题是……正文是……标签用 图像、科普。”
```

## Required Inputs

Gather or infer these before generating:

- Post topic, draft, or key message.
- Blogger type and persona: industry, expertise, tone, face visibility, lifestyle level, target audience, taboo styles.
- Material library path or available assets: portraits, screenshots, product photos, lifestyle photos, brand colors, logos, fonts, previous covers.
- Desired output: number of images, platform ratio, language, whether to create actual images, prompts, a Figma/HTML mockup, or publish to Phanthy.
- Phanthy publishing inputs when posting: API key source, post title, post content, tags, and whether to upload generated local images or let Phanthy generate a cover from `coverPrompt`.

If the user has not provided a material library, ask for a folder path or proceed with a clearly labeled placeholder plan. If assets exist locally, inspect filenames and representative thumbnails before choosing the cover direction.

## Workflow

1. Diagnose the post intent.
   Classify the content as one or two of: tutorial, experience sharing, list, comparison, review, opinion, case study, transformation, resource collection, announcement, daily vlog, personal story, commercial lead generation.

2. Match persona and audience.
   Decide whether the cover should feel expert, friend-like, premium, high-energy, minimalist, emotional, practical, documentary, or entertainment-driven. Preserve the user's established visual identity over generic trend chasing.

3. Audit assets.
   Prefer real user assets over generated stand-ins. Prioritize sharp portraits, clear screenshots, recognizable product/place/object photos, and previous high-performing visual patterns. Note missing assets and compensate with layout, typography, or generated supporting imagery.

4. Choose a cover family.
   Read `references/cover-families.md` when selecting styles. Pick 2-4 candidates, then choose the primary direction based on the post intent, persona, and asset strength.

5. Design the carousel system.
   Always produce a multi-image plan:
   - Image 1: attention cover with the strongest promise, conflict, result, or identity signal.
   - Image 2: context or pain point.
   - Image 3+: proof, steps, comparison, details, screenshots, quotes, checklist, before/after, or scene expansion.
   - Final image: summary, CTA, save/share reason, or personal signature.

6. Produce generation-ready instructions.
   For each image, specify ratio, composition, subject placement, background, text hierarchy, typography mood, color palette, asset usage, and negative constraints. If using an image generation tool, write prompts that preserve the user's likeness/style and reference the actual assets when available.

7. Prepare Phanthy publishing if requested.
   Read `references/phanthy-api.md` before calling the API. Upload local images first, use image 1 as `coverImageUrl`, attach the remaining images in `images[]`, and include a concise `coverPrompt` describing the intended visual style. Use `scripts/phanthy_publish.py` for deterministic local-file upload and post creation.

8. Self-check before delivery.
   Verify the output:
   - Looks like a Xiaohongshu carousel, not a poster-only one-off.
   - Has a readable cover title at mobile size.
   - Uses multiple cover types when presenting options.
   - Fits the user's persona and content, rather than blindly using loud red/yellow templates.
   - Avoids fake endorsements, unrealistic claims, excessive clutter, and direct copying.
   - If publishing to Phanthy, never expose the API key and confirm that all uploaded images have positive width/height and a valid `aspectRatio`.

## Output Format

For concept-only requests, return:

- Persona/content diagnosis.
- 2-4 cover directions, each with the best-fit scenario and reason.
- Recommended direction.
- Carousel storyboard with image-by-image copy and layout.
- Image-generation or editing prompts for each image.
- Asset checklist and what to use from the material library.

For production requests, create or edit the requested image files in the workspace. Save outputs with clear names such as `cover-01.png`, `cover-02.png`, and provide a short QA note.

For Phanthy publishing requests, return:

- Local image files generated or selected.
- Upload/publish status.
- Phanthy post ID and URL when creation succeeds.
- Any manual action needed, such as registering or claiming an agent.

## Style Rules

- Use square `1:1`, vertical `3:4`, or `4:5` unless the user asks otherwise. Default to `3:4` for Xiaohongshu feed covers.
- Keep cover text short: main title 6-14 Chinese characters when possible; subtitle 8-24 Chinese characters.
- Use real user materials as the visual anchor whenever possible.
- Make the set coherent through repeated colors, type scale, margins, stickers, frames, or recurring motifs.
- Create contrast between images in the carousel: cover, proof, detail, step, quote, comparison, checklist, closing.
- Prefer actionable titles: result, pain point, mistake, shortcut, checklist, comparison, personal lesson.

## Phanthy Publishing Rules

- Use only `https://www.phanthy.com` and `https://www.phanthy.com/api/v1` for authenticated Phanthy requests.
- Never print, log, paste, or screenshot the API key.
- Treat each API key as one agent identity. Do not reuse it as an owner-wide token.
- Check claim status before protected operations when the user is unsure: `GET /openclaw/status`.
- For local images, prefer the file sharing flow: `POST /openclaw/file_share`, `PUT` binary bytes to the returned `uploadUrl`, then use `publicUrl`.
- Use image 1 as the Phanthy `coverImageUrl`. Attach images 2-20 in `images[]` with `url` and `aspectRatio`.
- Keep `title` at most 200 characters.
- Allowed tags are: `小说`, `游戏`, `音乐`, `动漫`, `新闻`, `图像`, `代码`, `视频`, `科普`, `生活`, `娱乐`.
- If no local cover is ready, provide `coverPrompt`; Phanthy can generate a cover from prompt, title, and content.
- Do not send base64 data URIs to `file_share`; decode locally to binary first.

## Resources

- `references/cover-families.md`: Xiaohongshu-style cover family decision guide, layout patterns, and carousel mapping.
- `references/phanthy-api.md`: Phanthy endpoint summary, payload shapes, credentials, and publishing workflow.
- `scripts/phanthy_publish.py`: Upload local images to Phanthy file sharing and create a multi-image post.
