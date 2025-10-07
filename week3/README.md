# 🧑‍💻 Week 3: Introduction to LangChain – Generative AI 

---

## 🚀 What is LangChain?
LangChain is an open-source framework that helps developers build applications powered by large language models (LLMs). It provides modular components and end-to-end tools for creating complex AI applications.

---

**Key Features:**
1. Supports all major LLMs (OpenAI, Anthropic, Google, Hugging Face, and more)
2. Simplifies developing LLM-based applications
3. Integrates with major tools and data sources
4. Open source, free, and actively developed
5. Supports all major GenAI use cases

---

## 📚 Why Do We Need LangChain?

- **Uniformity:** It abstracts the complexity of working with different LLMs and APIs, providing a consistent interface.
- **Productivity:** Developers can quickly build, test, and deploy AI-powered apps without reinventing the wheel.
- **Flexibility:** Easily swap between different models and providers.
- **Ecosystem:** Integrates with databases, vector stores, APIs, and more.

---

## 🛠️ What Can You Build with LangChain?
- Conversational Chatbots
- AI Knowledge Assistants
- AI Agents (autonomous workflows)
- Summarization/Research Helpers
- Retrieval-Augmented Generation (RAG) systems

---

## 🏗️ LangChain Curriculum (This Series)
1. **Fundamentals** (today)
2. Basic RAG (Retrieval-Augmented Generation)
3. Advanced Use Cases

---

## 🧩 LangChain Components
LangChain is built around modular components. Today, we focus on the **Model Component**.

### What are Models?
The Model Component in LangChain is designed to make it easy to interact with various language models and embedding models. It provides a uniform interface for:
- LLMs (for text generation)
- Chat Models (for conversational AI)
- Embedding Models (for similarity search, RAG, etc.)

---

### 📊 Model Component Structure  

```text
Model Component
│
├── Language Models
│   ├── LLMs → (Chatbots, Text Generation)
│   └── Chat Models → (Conversational AI, Assistants)
│
└── Embedding Models → (Semantic Search, RAG)
```
---

# Comparison: LLMs (Base Models) vs. Chat Models (Instruction-Tuned)

| Feature | LLMs (Base Models) | Chat Models (Instruction-Tuned) |
|---|---|---|
| **Purpose** | Free-form text generation | Optimized for multi-turn conversations |
| **Training Data** | General text corpora (books, articles) | Fine-tuned on chat datasets (dialogues, user-assistant conversations) |
| **Memory & Context** | No built-in memory | Supports structured conversation history |
| **Role Awareness** | No understanding of "user" and "assistant" roles | Understands "system", "user", and "assistant" roles |
| **Example Models** | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B | GPT-4, GPT-3.5-turbo, Llama-2-Chat, Mistral-Instruct, Claude |
| **Use Cases** | Text generation, summarization, translation, creative writing, code generation | Conversational AI, chatbots, virtual assistants, customer support, AI tutors |

```
```

**Use Cases:**
- **Language Models (LLMs, Chat Models):**
  - Chatbots, AI assistants, text summarization, content generation
- **Embedding Models:**
  - Semantic search, document similarity, retrieval-augmented generation (RAG)

**Why is this useful?**
- You can switch between OpenAI, Anthropic, Google, Hugging Face, and open-source models with minimal code changes.
- You can use the same interface for both chat and text generation tasks.

**Summary:**
- LLMs are great for generating or summarizing text in one go (e.g., writing an article, summarizing a document).
- Chat Models are designed for back-and-forth conversations, remembering context and previous messages (e.g., chatbots, virtual assistants).

<img src="https://miro.medium.com/v2/resize:fit:1400/1*dKpTRkz-YfHVHMbcQciElA.png" width="500" alt="LLM vs Chat Model Chart"/> <div align="center"><sub>Image credit: MEDIUM</sub></div>

---

## 🌍 Supported Providers & Open Source Models

- **OpenAI** (e.g., GPT-3.5, GPT-4)
- **Anthropic** (e.g., Claude)
- **Google** (e.g., Gemini)
- **Hugging Face** (e.g., Falcon, Mistral, Llama)
- **Open Source Models:**
  - Llama 2, Mistral, Falcon, Vicuna, and more
  - Find them on [Hugging Face Model Hub](https://huggingface.co/models)

**Advantages of Open Source Models:**
- Free to use
- Can be run locally (privacy)
- Customizable and transparent

**Disadvantages:**
- May require more setup
- Sometimes less powerful than proprietary models

---

## 📚 Resources
- [LangChain Official Documentation](https://python.langchain.com/docs/introduction/)
