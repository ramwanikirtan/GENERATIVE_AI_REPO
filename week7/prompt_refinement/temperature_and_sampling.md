# Temperature & Sampling — Controlling Creativity
# Temperature & Sampling — Controlling Creativity

Temperature and sampling parameters influence the randomness of LLM outputs. In no-code UIs these are often exposed as a "creativity" or "temperature" slider.

Guidelines

- Temperature ~0.0–0.3: deterministic outputs (good for structured tasks)
- Temperature ~0.4–0.7: balanced (some creativity, reasonably stable)
- Temperature ~0.8–1.0+: highly creative and varied outputs (useful for ideation)

Top-p (nucleus sampling)

- If available, top_p restricts sampling to the top cumulative probability mass. Lower top_p is similar to lowering temperature but with different properties.

Examples to try (no-code)

1. Prompt: "Generate 5 creative taglines for an eco-friendly water bottle brand."
   - Run once with temperature = 0.2 (you'll get safe, similar options)
   - Run with temperature = 0.9 (you'll get more variety and riskier phrasing)

2. Structured task: "Extract dates from this text and output as a list."
   - Use temperature = 0.0 to minimize hallucination and ensure the model picks only explicit dates.

Practical tips

- For evaluation tasks and structured output, keep temperature low.
- For brainstorming and creative prompts, increase temperature and collect many outputs into a sheet to choose the best.
- Use multiple runs and majority voting (self-consistency) for robust answers on ambiguous questions.

Exercise

- Write one prompt and have them run it at three different temperatures. Paste outputs into a sheet and compare novelty vs correctness.
