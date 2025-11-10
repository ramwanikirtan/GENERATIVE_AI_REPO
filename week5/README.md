# Week 5: Structured Output & the LangChain Structured Output Parser (Manual)

## Overview
This week is a hands-on manual covering LangChain's structured output capabilities — how to request typed, machine-readable responses from large language models and how LangChain parses those responses into Python-native structures (JSON, Pydantic models, TypedDicts).

The goal: move from brittle free-form text parsing to a predictable contract between your application and the model. Instead of asking the model to "write a summary", you ask it to produce an object that matches an explicit schema. That enables validation, programmatic access, and safer automation.

This document expands the week material into a short manual: conceptual background, "contract" for inputs/outputs, walkthroughs of the provided examples, debugging and validation techniques, and exercises.

## Contract (quick)

Inputs:
- A chat model (e.g., `ChatOpenAI`, `ChatHuggingFace`) configured with API credentials.
- A schema describing the desired output shape: JSON Schema, a Pydantic model, or a TypedDict/Annotated type.
- A free-text prompt (the content you want summarized/parsed).

Outputs:
- A typed object (dict / Pydantic model / TypedDict) where fields correspond to the schema. The library will attempt to coerce and validate types where supported.

Error modes:
- Validation errors (Pydantic raises a validation error when required types are missing/invalid).
- Partial output (model omits optional fields or returns null for nullable fields).
- Parsing failure (model returns text that cannot be coerced into the schema) — treat as an invalid response and either retry or fail-safe.

Success criteria:
- The returned object matches the schema; required fields are present and validated.

## Key topics covered in this week

1. The structured-output pattern: why and when to use it. Benefits vs the free-text approach.
2. JSON Schema vs Pydantic vs TypedDict: strengths and trade-offs.
3. How LangChain's `with_structured_output` works (high-level):
   - It augments the prompt with instructions telling the model to return the schema.
   - It parses the returned string into the requested type.
   - If using Pydantic, it validates/coerces fields.
4. Practical prompts and examples included in the repository for hands-on learning.

## Files and walkthrough (detailed)

- `json_schema.json`
  - A tiny JSON Schema example for a `student` object. Use this to see how generic schema definitions map to parsed output.

- `pydantic_demo.py`
  - Demonstrates a `Student` Pydantic model and how Pydantic coerces/validates types (e.g., string->int coercion). This file is intentionally minimal to show basics of `BaseModel` usage.

- `typeddict_demo.py`
  - Shows a `TypedDict` usage pattern for simple static typing. TypedDicts do not perform runtime validation — they are primarily for static type checkers and documentation.

- `with_structured_output_json.py`
  - Uses a JSON Schema object (inline in the script) and calls `model.with_structured_output(json_schema)`.
  - The returned `result` is a parsed object (usually a dict). This is the most portable approach (language-agnostic schema).

- `with_structured_output_pydantic.py`
  - Declares a `Review` as a Pydantic `BaseModel` (with descriptions and optional fields).
  - Passes the `Review` class to `model.with_structured_output(Review)` so the model's returned data is validated and accessible as `result` (Pydantic object). This is the most Pythonic approach.

- `with_structured_output_typeddict.py`
  - Uses `TypedDict` + `Annotated` metadata as the schema. This demonstrates a lightweight typing-first option; it relies on LangChain to map the type hints to a parsing instruction.

- `with_structured_output_llama.py`
  - Similar to the Pydantic example but uses a `ChatHuggingFace` adapter with a Llama-style endpoint. This file demonstrates that structured output patterns are usable with non-OpenAI models — but results and reliability may vary.

- `students_dataset.csv`
  - Placeholder CSV you can use to craft prompts that extract or summarize structured records.

- `.env`
  - Local credentials loader. Do not commit secrets.

## How LangChain parses structured output (mechanics)

At a high level:

1. LangChain generates an instruction appended to your prompt that describes the schema and how the model must format its output (e.g., JSON with exact fields).
2. The model is prompted to return only the structured representation.
3. LangChain receives the text response and runs a parser that attempts to convert it to the requested type:
   - For JSON Schema: parse text as JSON and validate the schema.
   - For Pydantic: parse into a dict then instantiate the BaseModel (Pydantic handles coercion/validation).
   - For TypedDict: parse as JSON/dict and return the dictionary (no runtime validation unless you add it).

Why Pydantic is useful: Pydantic will coerce compatible types (e.g., strings containing digits into ints) and will raise clear validation errors when required values are missing or types are incompatible.

## Prompt-engineering tips for reliable structured output

- Be explicit: include field names, types, and short descriptions in the schema.
- Use `required` fields where you absolutely need a value.
- Keep the output format directive short but precise — example: "Return only valid JSON matching the schema."
- If the model returns prose or commentary, instruct it to add a separate `notes` field rather than including free text inside structured fields.
- For local or weaker models (Llama variants) add redundancy in the prompt (provide the schema twice or show an example of the expected JSON output).

## Common edge cases and how to handle them

- Model returns non-JSON: attempt a retry with a stricter instruction; consider post-processing heuristics (extract JSON substring) as a fallback.
- Partial keys: treat missing optional keys as None/defaults; for required keys, retry the call or use a fallback path.
- Numeric parsing: if the model returns numbers as words or strings, Pydantic may coerce; otherwise, write a small sanitizer function.
- Arrays with single items: models sometimes drop brackets; detect and normalize (wrap single items in a list if schema expects an array).

## Debugging checklist

1. Print the raw model response — often the problem is format, not content.
2. Validate the raw text as JSON (try a quick `json.loads`); if it fails, search for the first/last brace pair and extract JSON.
3. Use a smaller example prompt that forces a simpler output to iterate quickly.
4. If Pydantic raises an error, inspect `e.errors()` to see which fields failed and why.

## Tests & validation ideas

- Unit test that calls the Pydantic example with the sample review and asserts: `result.summary` is non-empty, `result.sentiment in {'pos','neg'}`.
- Write a test that feeds deliberately malformed model output to the parser and asserts the library raises a parse/validation exception.

## Exercises (expanded)

1. Add a `rating` field to the `Review` schema (Pydantic) and ensure the model can return `"4"` and Pydantic coerces it to int.
2. Build a mini ETL: read `students_dataset.csv`, craft prompts that ask the model to extract each CSV row into a `Student` object, and accumulate validated objects.
3. Compare results between `ChatOpenAI` and `ChatHuggingFace` for the same schema; document success rates and common failure modes.

## How to run (quick)

```powershell
# activate venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # or pip install the lists shown in the previous README

# Run the Pydantic structured output demo
python week5/langchain-structured-output/with_structured_output_pydantic.py
```

## Final notes

Structured output parsers bridge the gap between LLM creativity and application correctness. With a small investment in schemas and validation code you can use LLMs in production flows that need predictable, typed outputs.

If you'd like, I can now:
- Add a small `tests/test_pydantic_output.py` that runs the Pydantic demo and asserts shape.
- Create a short demo notebook that runs each example and prints parsed results for students to inspect interactively.
# Week 5: LangChain — Structured Output

## Overview
This week focuses on producing structured, type-safe outputs from LLMs using LangChain's structured output helpers. Instead of free-form text, we design schemas (JSON Schema, Pydantic models, TypedDicts) so the model returns predictable, machine-readable data. That makes downstream parsing, validation, and programmatic use much easier and more robust.

You'll learn:
- Why structured outputs matter
- How to express schemas with JSON Schema, Pydantic and TypedDict
- How to use LangChain model adapters that accept a schema and return validated objects
- How to run the examples with both OpenAI and a Hugging Face LLM endpoint

## Key Concepts

- Structured output: asking the model to return data that conforms to a schema (e.g., a JSON object with specific fields and types).
- Schema types covered in the examples:
  - JSON Schema (generic, language-agnostic)
  - Pydantic BaseModel (Python-first, validation + type coercion)
  - TypedDict (simple, typing-only specification)
- Benefits:
  - Safer downstream processing (fewer parse errors)
  - Automatic validation and coercion (Pydantic)
  - Easier integration with data pipelines and UIs

## Files in this folder

- `json_schema.json` — a small JSON Schema example describing a `student` object.
- `pydantic_demo.py` — a short demo showing how to declare a Pydantic `Student` model and use it for parsing/validation.
- `typeddict_demo.py` — a minimal `TypedDict` example (Python typing usage).
- `with_structured_output_json.py` — LangChain example that registers a JSON Schema with the model and invokes `with_structured_output` to get structured results.
- `with_structured_output_pydantic.py` — same concept using a Pydantic `Review` model; the returned object is validated and accessible as a Pydantic instance.
- `with_structured_output_typeddict.py` — same concept using a `TypedDict`-style schema.
- `with_structured_output_llama.py` — demonstrates using a Hugging Face/TinyLlama endpoint via LangChain to produce structured output (shows compatibility beyond OpenAI).
- `students_dataset.csv` — placeholder dataset (empty in repository) you can use for testing or exercises.
- `.env` — local env file used by examples to load API keys (do NOT commit secrets to git; use environment variables or GitHub Secrets).

## How the examples work (short explanation)

1. Define a schema describing the structure you want back from the model. You can use JSON Schema, Pydantic models, or TypedDict annotations.
2. Call `model.with_structured_output(schema)` where `model` is a LangChain chat model (e.g., `ChatOpenAI`, `ChatHuggingFace`).
3. Invoke the structured model with a free-text prompt. LangChain will:
   - send a prompt that instructs the model to fill the schema,
   - parse the model's textual response into the requested structured type,
   - validate/coerce the result (Pydantic performs validation/coercion),
   - return a language-native object you can work with in Python.

This flow makes it safe to treat model results as typed objects instead of brittle strings.

## Quick start — prerequisites

1. Create a Python environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

2. Install dependencies used in the examples:

```powershell
pip install langchain langchain-openai pydantic python-dotenv langchain-huggingface
```

3. Provide API credentials (do NOT commit real keys):

Create a `.env` file (or set environment variables). Example `.env` keys used by the examples:

```
OPENAI_API_KEY=sk-...
HUGGINGFACEHUB_API_TOKEN=hf_...
HUGGINGFACE_API_URL=... (if using an endpoint)
```

Notes:
- Prefer using environment variables/GitHub Secrets rather than committing a `.env` file.
- If you do use `.env` locally, add it to `.gitignore` (already done in the repo).

## Run the examples

- JSON Schema example (OpenAI):

```powershell
python week5/langchain-structured-output/with_structured_output_json.py
```

- Pydantic example (OpenAI):

```powershell
python week5/langchain-structured-output/with_structured_output_pydantic.py
```

- TypedDict example (OpenAI):

```powershell
python week5/langchain-structured-output/with_structured_output_typeddict.py
```

- Hugging Face / Llama example:

```powershell
python week5/langchain-structured-output/with_structured_output_llama.py
```

Each script prints the parsed/validated result or demonstrates how to access fields programmatically (for instance `result['name']` or `result.name` depending on the schema type).

## Practical tips & gotchas

- Model reliability: structured output reduces parsing errors but models can still hallucinate or return unexpected values. Use `required` fields and validation where possible.
- Validation/coercion: Pydantic will coerce strings to ints where appropriate (e.g., `'32'` -> `32`) which is handy for messy inputs.
- Enum-like fields: prefer Literal/enum or `enum` in JSON Schema to constrain allowed values (e.g., sentiment should be one of `['pos','neg']`).
- Nullability: JSON Schema and Pydantic support optional/null fields — model may omit those keys, so handle defaults.
- LLM choice: OpenAI models have strong structured output support. Hugging Face / local models may need careful prompt engineering and may be less reliable for strict validation; test thoroughly.



## Further reading

- LangChain structured output docs: https://python.langchain.com/docs/
- Pydantic docs: https://pydantic-docs.helpmanual.io/
- JSON Schema: https://json-schema.org/

