# Zero‑Shot Prompting

TL;DR

Zero-shot prompting means asking a model to perform a task without giving it task-specific examples. Use it when the task is simple, well-specified, or when you want the model's unconstrained reasoning. For more reliability on structured tasks, prefer few-shot or chain-of-thought patterns.

What it is

- Definition: A single prompt that explains the task and asks for an output, with no exemplar inputs/outputs included.
- Strengths: fast to author, fewer tokens used, works well for broad tasks like summarization, classification of clear instructions, or idea generation.
- Weaknesses: can be brittle for complex or ambiguous tasks; higher risk of missing required format or hallucination.

When to use zero-shot

- Quick experiments and ideation (brainstorming, taglines, concept lists).
- Tasks where the correct output is obvious from a short instruction (e.g., "translate to French").
- When you want to test the model's default behavior before adding examples.

Zero‑shot prompt structure (simple template)

1. One-line instruction describing the task.
2. Brief constraints and output format.
3. Optional context or short input.

Example templates

- Summarization:

	Summarize the following text in 2–3 sentences, focusing on the main argument and one supporting fact:

	[PASTE TEXT]

- Classification (single label):

	Read the review below and output one of {Positive, Neutral, Negative}. Answer with a single word.

	Review: "[PASTE REVIEW]"

- Data extraction (single pass):

	Extract all dates mentioned in the text and list them as ISO dates, one per line:

	[PASTE TEXT]

No‑code examples to try

1) Idea generation — Chat UI / Playground

	 Prompt: "List 10 creative names for a sustainable coffee brand. No more than 3 words each."

2) Quick classification — Chat UI

	 Prompt: "Classify this tweet as Positive, Neutral, or Negative. Reply with exactly one word.\nTweet: 'Finally got my hands on the new eco-bottle — love it!'"

3) Extraction — Document UI

	 Prompt: "From the text below, extract the person's full name and email address and output as JSON with keys name and email.\nText: [PASTE TEXT]"

Tips to improve reliability (without examples)

- Be explicit about the output format (JSON, CSV, one-per-line). Models follow concrete format instructions better.
- Use short constraints: "Answer in one sentence", "Return only the label", "No extra commentary".
- Lower temperature for deterministic outputs when format matters. Increase temperature for creative lists.
- If you see repeated errors, move to few-shot (provide 2–4 examples) or structured-output patterns.

Evaluation exercises (classroom)

1. Run one prompt in zero‑shot and again in few‑shot; compare correctness and variance.
2. Use a noisy text and extract structured fields with zero‑shot; discuss failure cases and when to switch to examples or regex post-processing.
3. Design a zero‑shot prompt for a multi-lingual summary (short instruction + language) and evaluate fidelity across languages.


