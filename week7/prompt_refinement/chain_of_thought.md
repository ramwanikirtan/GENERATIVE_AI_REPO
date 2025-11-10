# Chain-of-Thought (CoT) Techniques

Chain-of-thought prompting asks the model to reveal intermediate reasoning steps before giving a final answer. CoT can improve performance on multi-step reasoning tasks but may increase token usage and expose intermediate incorrect reasoning.

Variants

- Full CoT: ask the model to show detailed steps.
- CoT-lite / stepwise: request a short numbered list of steps followed by a single-sentence answer.
- Self-consistency: sample multiple CoT outputs and aggregate answers (no-code: re-run several times and vote).

Examples (no-code-friendly)

1) Math / logical reasoning (CoT-lite)

Prompt:
"Solve the problem. Show brief reasoning (2–4 steps), then give the final answer.\nProblem: If a train leaves at 9am traveling 60km/h for 2 hours, how far does it travel?\nReasoning:\n1.\n2.\nFinal Answer:"

2) Decision tasks

Prompt:
"Compare two candidate solutions and list pros/cons (3 bullets each), then give a recommended choice in one sentence. Problem: <describe problem>"

Risks and mitigation

- CoT can surface hallucinated or incorrect intermediate steps. Always verify final answers for critical tasks.
- Use CoT for analysis; use a separate verification prompt to fact-check final claims (e.g., "Is this conclusion supported by the facts above? Answer yes/no and why.").

No-code self-consistency (manual)

1. Run the same CoT prompt 5 times in the playground with different randomness settings or by clicking Regenerate.
2. Collect final answers in a Sheet and use majority-vote to select the most frequent final answer.

E
