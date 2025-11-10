# Few-shot Prompts — Teach by Example

Few-shot prompting provides the model with a small number of examples (1–5) demonstrating the task. This is especially effective for formatting tasks, classification with nuanced labels, and when you want the model to mimic a pattern.

Few-shot patterns

- One-shot: single example + target input
- Two-shot / k-shot: multiple examples showing variations
- Patterned examples: include diverse edge cases so the model generalizes

How to structure a few-shot prompt

1. Optionally set a short system persona.
2. Provide clear instruction of the task.
3. Add 1–5 examples in the exact output format you expect.
4. Provide the final query to be completed in the same pattern.

Examples (copy/paste)

1) One-shot (classification)

Prompt:
"Classify sentiment as Positive / Neutral / Negative.\nExample:\nText: 'I loved the film.'\nSentiment: Positive\nNow classify:\nText: 'The service was slow.'\nSentiment:"

2) Two-shot (structured extraction)

Prompt:
"Extract title and author as JSON.\nExample 1:\nText: 'Article: The Rise of AI — Author: Jane Doe'\nOutput: {\"title\": \"The Rise of AI\", \"author\": \"Jane Doe\"}\n\nExample 2:\nText: 'Article: Climate Action Today — Author: John Smith'\nOutput: {\"title\": \"Climate Action Today\", \"author\": \"John Smith\"}\n\nNow extract:\nText: '<paste article text>'\nOutput:"

3) Few-shot with format enforcement (tips)

- Keep examples minimal but exact.
- Use consistent casing and punctuation in examples so the model picks up the pattern.
- When possible, label outputs explicitly (e.g., "Output:").

When few-shot helps most

- Tasks where zero-shot fails due to ambiguity in label interpretation.
- Tasks requiring consistent formatting (CSV, JSON, bullet lists).

