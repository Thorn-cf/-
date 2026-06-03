# Long-Form Workflow

Use this when the manuscript is long, arrives in batches, or the user requests many versions.

## Chunking

- Split by existing headings first, then by paragraph groups.
- Keep each chunk semantically complete; do not cut inside a complex argument.
- Maintain a running structure map with section title, purpose, key claims, examples, and target status.
- Maintain stability locks across chunks: facts, terms, stance, recurring names, and logic relationships.

## Batch Protocol

For each batch:

1. Confirm the batch position, such as "第 1/5 部分".
2. Extract the local outline and update the global structure map.
3. Rewrite according to the selected mode.
4. Check continuity with previous batches: terminology, names, tone, and argument progression.
5. Save unresolved questions for the next batch instead of guessing.

## Version Control

When producing multiple drafts:

- Draft a shared structure map once.
- Reuse the same heading hierarchy for every version.
- Track mode-specific decisions, such as "Version B uses deeper metaphor replacement" or "Version C uses public-account tone".
- Keep terminology and factual claims stable across versions unless a mode requires localization.
- Keep a version matrix that records the strategy, tone, target platform, and originality strength for each draft.

## Very Large Inputs

If the input is too large for one response:

- Ask the user to send the manuscript in numbered parts.
- Do not begin final full-draft generation until enough structure is known, unless the user asks to process as they paste.
- After each part, return the rewritten part and a compact continuity note.
- At the end, offer a whole-article consistency pass.

## Continuity Checks

Before finalizing long-form output, check:

- Heading hierarchy is complete and unchanged unless requested.
- Key terms are translated or rewritten consistently.
- Examples still support the same claims.
- Transitions between sections are smooth.
- The ending resolves the same central question as the source.
- Similarity-risk repairs have been applied to any section that remains too close to the source.
