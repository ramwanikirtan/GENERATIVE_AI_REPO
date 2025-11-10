# Prompt Chaining & Decomposition

Prompt chaining (or decomposition) breaks a complex task into smaller steps and runs separate prompts for each step. This improves reliability and traceability.

Use cases

- Long-form generation with intermediate planning
- RAG pipelines: retrieve → extract → synthesize
- Multi-turn transformations (e.g., extract facts → rewrite into summary)

No-code example (Zapier / Make)

Flow:

1. Trigger (manual / form)
2. Action A: Run Prompt 1 (e.g., extract key facts)
3. Action B: Run Prompt 2 using output of A (e.g., write a summary using those facts)
4. Action C: Save final result to Google Sheets

Prompt chaining pattern (manual)

- Step 1 (Extract): "From this text, list the 5 key facts as bullets. <text>"
- Step 2 (Summarize): "Using the facts below, write a 100-word summary with one suggested action. Facts: <paste facts>"

Advantages

- Each step is easier for the model to do reliably.
- Easier to validate intermediate outputs.
- Facilitates human-in-the-loop corrections at intermediate stages.

Practical tips

- Keep each step focused and small.
- Define clear interfaces between steps (what data shape is passed).
- Save intermediate outputs for audit and debugging.

Exercise

- Build a 2-step chained workflow in Zapier: Form -> Extract facts -> Summarize -> Sheet. Test with 5 inputs and inspect intermediate facts for errors.
