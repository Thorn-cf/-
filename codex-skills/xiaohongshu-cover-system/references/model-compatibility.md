# Model Compatibility Guide

Use this file when the model is weak, the request is vague, the context window is small, or the model is unsure how to choose a cover style. Follow the templates literally.

## Fast Path

1. Extract topic in one sentence.
2. Choose persona. If unknown, use `实用型知识博主`.
3. Choose content type from this list: `教程`, `清单`, `观点`, `测评`, `案例`, `个人故事`, `资源合集`, `生活记录`.
4. Choose one cover family from the fallback table below.
5. Create 6 images at `3:4`.
6. Make image 1 the strongest cover.
7. Make image 2 explain the pain/context.
8. Make images 3-5 provide proof, steps, examples, or comparison.
9. Make image 6 summarize and invite save/share/comment.
10. If publishing to Phanthy, upload only after local images and API key are available.

## Fallback Cover Family Table

| Content type | Default cover family | Backup family |
| --- | --- | --- |
| 教程 | Screenshot Annotation | Checklist / List Card |
| 清单 | Checklist / List Card | Big Typography Promise |
| 观点 | Big Typography Promise | Comment / Chat Style |
| 测评 | Product / Object Flatlay | Before / After Split |
| 案例 | Before / After Split | Clean Expert Card |
| 个人故事 | Portrait + Quote | Diary / Handwritten Collage |
| 资源合集 | Checklist / List Card | Screenshot Annotation |
| 生活记录 | Diary / Handwritten Collage | Magazine Collage |
| unknown | Big Typography Promise | Clean Expert Card |

## Asset Decision Rules

- If portraits exist, use a portrait on image 1 or image 6.
- If screenshots exist, use screenshots for tutorial, tools, proof, or case-study pages.
- If product/object photos exist, use them for review and recommendation posts.
- If only text is available, use typography cards and simple shapes.
- If assets are missing, explicitly say: `素材缺口：未提供真实素材，先用占位视觉/生成图替代`.

## Fixed Output Template

Use this exact structure for planning answers:

```text
内容诊断
- 主题：
- 人设：
- 内容类型：
- 推荐封面家族：
- 选择理由：

多图封面方案
1. cover-01.png
   角色：封面
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

2. cover-02.png
   角色：背景/痛点/上下文
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

3. cover-03.png
   角色：步骤/证据/例子
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

4. cover-04.png
   角色：步骤/对比/细节
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

5. cover-05.png
   角色：证明/清单/结果
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

6. cover-06.png
   角色：总结/CTA
   画面：
   主标题：
   副标题：
   使用素材：
   生成提示词：

万神殿发布准备
- 是否发布：
- API key 来源：
- 标题：
- 正文：
- 标签：
- 上传方式：
- 注意事项：
```

## Prompt Formula

Use this short formula when the model struggles to write detailed prompts:

```text
小红书风格多图封面，3:4 竖图，[封面家族]。
主题：[主题]。
人设：[人设]。
本图角色：[角色]。
画面：[主体] 放在 [位置]，背景是 [背景]，文字区域在 [位置]。
文字：主标题「[主标题]」，副标题「[副标题]」。
风格：[颜色]，[字体气质]，[装饰元素]。
限制：手机端可读，不要复制具体博主，不要虚假背书，不要乱码文字。
```

## Safe Defaults

- Ratio: `3:4`
- Image count: `6`
- Text density: cover low, detail pages medium
- Palette: white/cream background + one accent color + black text
- Font mood: bold rounded Chinese title, clean sans-serif body
- Title length: 6-14 Chinese characters
- Subtitle length: 8-24 Chinese characters
- CTA: `收藏备用`, `照着做`, `评论区告诉我`

## Low-Capacity Failure Prevention

Avoid these mistakes:

- Do not output only one cover image.
- Do not skip image-specific copy.
- Do not say "use Xiaohongshu style" without naming layout, text, subject, and assets.
- Do not call Phanthy APIs before local image files exist unless using `coverPrompt` only.
- Do not include the Phanthy API key in the final response.
- Do not use tags outside `小说 游戏 音乐 动漫 新闻 图像 代码 视频 科普 生活 娱乐`.
- Do not claim the image was uploaded unless an upload response succeeded.

