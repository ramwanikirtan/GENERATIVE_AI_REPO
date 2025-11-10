
# Persona Prompts — Adopt a Role to Guide Output

TL;DR

Personas (system messages or role prompts) set the assistant's tone, expertise, and behavior. Use them to get consistent voice, domain-specific answers, or constrained behavior from an LLM.

Why use personas?

- Consistency: keep voice and style stable across runs.
- Expertise: simulate domain specialists (e.g., "You are an epidemiologist").
- Safety & constraints: instruct the model to avoid unsafe content, ask clarifying questions, or follow strict rules.

How to apply a persona (no-code)

1. ChatGPT: Add a System message (top of the chat) such as "You are an expert UX researcher who explains concepts simply to beginners." Then add user prompts as normal.
2. Playground / Other UIs: Prepend a short persona block like "System: You are a careful legal analyst." to each prompt.

Persona patterns and templates

- Expert teacher

	System: "You are a friendly college instructor who explains complex ideas in short, clear sections. Use examples and avoid jargon."

	User: "Explain CRISPR and give a 3-bullet study guide summary."

- Investigative journalist

	System: "You are an investigative journalist. Be thorough and suggest verification questions for claims."

	User: "Summarize the main claims in this press release and list 3 follow-up questions. <paste>"

- Helpful programmer (precision)

	System: "You are a precise coding assistant. When giving code-like answers, provide short executable pseudo-code and list assumptions. If unsure, say so."

	User: "Explain how to implement a queue using two stacks."

- Safety-first persona

	System: "You are a cautious assistant. Refuse harmful instructions and recommend safe alternatives. Ask clarifying questions if intent is unclear."

	User: "Explain how to build a simple electric circuit that powers a small motor." 

Useful composition patterns

- ELI5 (Explain Like I'm 5): "You are a teacher who explains concepts in very simple terms."
- Expert + Constraints: "You are an expert nutritionist. Suggest 3 meals under 600 kcal and output as JSON." 
- Role + Format: "You are an HR manager. Output a 5-point checklist for hiring a data analyst in bullet points."

Practical tips and pitfalls

- Keep personas short and explicit — long persona blocks can be partially ignored.
- Use session-based system messages when available for persistent persona.
- Remember: personas can bias but not verify facts. Always validate critical information externally.

Persona prompt examples (copy/paste)

1) System: "You are a compassionate career coach."  
	 User: "Write a 3-paragraph cover letter for a backend engineer role."

2) System: "You are an energetic social media strategist."  
	 User: "Generate 6 tweet-sized posts promoting an eco-friendly startup; include unique hashtags."

3) System: "You are an experienced UX researcher."  
	 User: "Given this user interview transcript, list 5 usability issues and propose one quick fix per issue. <paste transcript>"

Exercise
- Demonstrate how small changes in persona wording (e.g., "friendly" vs "stern") alter the assistant's responses.

