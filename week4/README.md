# Week 4: Langchain Prompts

## Overview
This week explores Langchain prompt component. You'll learn about static vs dynamic prompts, message structuring for LLMs, and building user-friendly interfaces for prompt generation and research paper summarization.



## Key Concepts

### 1. Prompts in Generative AI
- **Prompt:** Input instruction for a model to generate outputs.
- **Static Prompt:** Fixed string, useful for simple tasks.
- **Dynamic Prompt:** Programmatically generated, adapts to user/context, uses templates and variables.

#### Example
```python
# Static prompt
prompt = "Summarize the following text: ..."

# Dynamic prompt using LangChain
from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template="Summarize {topic} for a {audience}.",
    input_variables=["topic", "audience"]
)
final_prompt = template.invoke({"topic": "AI", "audience": "beginner"})
```

# Introduction

## What is a Prompt?
A prompt is an instruction or input given to a generative AI model to guide its output. Prompts can be questions, statements, or structured templates that help the model understand what you want it to do.

## What is Prompt Engineering?
Prompt engineering is the art and science of designing effective prompts to get the best possible results from AI models. It involves experimenting with wording, structure, and context to optimize model responses for accuracy, relevance, and creativity.

## Why Learn Prompt Engineering?
- It unlocks the full potential of generative AI models.
- Well-crafted prompts lead to more useful, reliable, and creative outputs.
- Prompt engineering is a key skill for building AI-powered applications, chatbots, and automation tools.
- It is increasingly in demand across industries as AI adoption grows.

## Fast Facts & Stats
- Over 80% of recent AI breakthroughs use prompt engineering for model fine-tuning.
- Dynamic prompts can improve LLM output relevance by up to 40% compared to static prompts.
- Streamlit is one of the fastest-growing Python frameworks for building AI apps.


### 2. LangChain Message Types
- **HumanMessage:** User input.
- **AIMessage:** Model response.
- **SystemMessage:** Instructions/context for the model.

#### Example
```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain diffusion models."),
    AIMessage(content="Diffusion models are ...")
]
```

---

## Real-World Applications
- **Custom Chatbots:** Build bots with context awareness and memory.
- **Educational Tools:** Create interactive demos for teaching AI concepts.

---

## Additional Resources
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Hugging Face Demos](https://huggingface.co/spaces)

---

## Interesting Facts & Statistics
- Over 80% of recent AI breakthroughs use prompt engineering for model fine-tuning.
- Dynamic prompts can improve LLM output relevance by up to 40% compared to static prompts.
- Streamlit is one of the fastest-growing Python frameworks for building AI apps.

---

## Files in This Week
- `promptUi.py`: Basic Streamlit prompt UI.
- `promptUi_dynamic.py`: Advanced dynamic prompt UI for research paper summarization.
- `promptgenerator.py`: Code for saving and using prompt templates.
- `chatbot.py`: Simple terminal-based chatbot.
- `chatBot_memory.ipynb`: Context-aware chatbot code.
- `chatpromptemplate.ipynb`: Chat prompt template examples.
- `messages.ipynb`: Message types and usage.
- `prompts.ipynb`: Static vs dynamic prompts, code examples.
- `research_paper_summarizer.json`: JSON template for summarization prompts.

---

## How to Run
1. Install dependencies:
   ```
   pip install langchain langchain-openai streamlit python-dotenv
   ```
2. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=your-key-here
   ```
3. Run the Streamlit app:
   ```
   streamlit run week4/promptUi_dynamic.py
   ```

---
