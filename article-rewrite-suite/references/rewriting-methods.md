# Rewriting Methods

Use these methods to make translation, rewriting, washing, and imitation more stable than sentence-level paraphrasing.

## Structure Skeleton

Before drafting, convert the source into a non-publishable skeleton:

```text
Title intent:
Central thesis:
Audience and tone:
Section map:
- Section title:
- Section purpose:
- Key claims:
- Evidence or examples:
- Emotional movement:
- Transition role:
Conclusion move:
```

Draft from this skeleton, not from the original sentences. Preserve the skeleton's order and functions unless the user asks to change structure.

## Paragraph Function Rewrite

Label each paragraph by function, then write a fresh paragraph that performs the same job:

- Problem framing
- Thesis or judgment
- Cause explanation
- Evidence or example
- Comparison or contrast
- Counterargument
- Transition
- Emotional resonance
- Summary
- Call to action

This is the default method for "洗稿", "深度改写", and "降重". Avoid synonym replacement as the main strategy.

## Reverse Outline Method

For high-originality rewrites:

1. Compress the source into a reverse outline.
2. Convert the outline into claim cards and example cards.
3. Put the original text aside.
4. Draft a new article from the cards.
5. Compare the new draft against the source only during quality checking.

Use this when the user wants multiple new drafts or strong originality.

## Stability Locks

Create locks before rewriting:

```text
Fact locks: names, dates, numbers, terms, cited positions, definitions
Logic locks: causality, chronology, comparisons, conditions
Stance locks: attitude, recommendation, criticism, uncertainty level
Term locks: required translations or recurring phrases
```

Never alter locked items unless the user explicitly asks for adaptation or localization.

## Style Fingerprint

For imitation, extract style without copying wording:

- Sentence length: short, medium, long, mixed
- Paragraph density: sparse, compact, essay-like, platform-like
- Rhythm: calm, punchy, lyrical, analytical, conversational
- Rhetoric: questions, parallelism, contrast, metaphor, aphorism
- Evidence style: data, anecdotes, examples, expert framing, lived experience
- Emotional curve: restrained, persuasive, intimate, urgent, reflective
- Opening and closing pattern

Apply these parameters to the new draft. Do not reuse signature lines, rare metaphors, or recognizable anecdotes.

## Multi-Version Differentiation

When producing multiple drafts, make each version differ by strategy instead of surface tone:

```text
A version: faithful polish, closest to source meaning
B version: deep reconstruction, highest originality
C version: platform adaptation, optimized for target channel
D version: story-driven, stronger narrative pull
E version: analytical, clearer logic and hierarchy
F version: concise, compressed but complete
```

Keep the macro-structure stable across versions unless the user requests structural variety.

## Similarity-Risk Scan

Before delivery, scan for high-risk similarity:

- Same sentence openings across many paragraphs
- Same sequence of clauses or examples
- Distinctive metaphors, jokes, slogans, or aphorisms retained
- Section endings that land on the same wording
- Keyword clusters copied too closely
- Paragraph rhythm that shadows the source line by line

If a section is risky, repair it by returning to the paragraph function and rewriting the section again.

## Failure Repair Loop

Use targeted repair instead of regenerating the whole draft:

```text
Problem: too similar
Repair: change paragraph opening, sentence order, transitions, and rhetorical device

Problem: meaning drift
Repair: restore fact and logic locks

Problem: quality drop
Repair: strengthen examples, transitions, rhythm, and specificity

Problem: structure drift
Repair: align headings and paragraph functions with the structure skeleton
```

After repair, run the quality rubric again.
