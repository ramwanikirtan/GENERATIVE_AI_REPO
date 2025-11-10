# Structured Output Techniques (JSON / CSV / Tables)

When downstream systems require machine-readable output, instruct the model to produce structured formats and validate them manually (no-code) or with lightweight tools.

Best practices

- Clearly state the required format (e.g., "Output only valid JSON").
- Provide a short example of the expected structure in the prompt.
- If possible, request an explicit schema and a fallback error object (e.g., {"error":"parsing_failed"}).

Prompt examples

1) Simple JSON extraction

Prompt: "Extract title and summary from this article. Output ONLY valid JSON with fields: title (string), summary (string). Article: <text>"

2) CSV-style output (for spreadsheet import)

Prompt: "From the list of attendees below, produce CSV rows with columns: name, email, affiliation. Output rows only, no header. Attendees: <list>"

3) Markdown table

Prompt: "Create a markdown table with columns Feature | Description | Priority from the following feature list: <list>"

Validation (no-code)

1. Paste the assistant output into an online JSON validator or into a Google Sheets cell.
2. If invalid, re-run with a stricter instruction: "Output ONLY valid JSON and nothing else." Optionally include: "If you cannot, reply with {\"error\":\"parsing_failed\"}."

Appendix: Example JSON schema (human-readable)

{
  "title": "string",
  "summary": "string",
  "published_year": "integer (optional)"
}
