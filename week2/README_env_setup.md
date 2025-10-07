# 🛠️ Environment Setup for Week 2

Follow these steps to set up your Python environment for the course and hands-on labs.

---

## 🗂 Step 1: Create Course Folder

Open Anaconda Prompt (or terminal):

```bash
cd Desktop   # or Documents (anywhere you want)
mkdir intro-to-genai
cd intro-to-genai
```

---

## 📝 Step 2: Create requirements.txt

Inside the `intro-to-genai` folder, create a file called `requirements.txt` and paste this:

```text
# Core LangChain
langchain
langchain-core
langchain-community
langchain-openai
langchain-google-genai

# Vector DBs
faiss-cpu
chromadb
pinecone-client

# Hugging Face
transformers
huggingface_hub

# Deep Learning (CPU safe)
torch
torchvision
tensorflow

# Web/API tools
flask
streamlit

# Data & Utils
numpy
pandas
scikit-learn
matplotlib
seaborn
python-dotenv

# Jupyter support
ipykernel
```

---

## 🐍 Step 3: Create Conda Environment

Back in Anaconda Prompt:

```bash
# Make new environment with Python 3.10
conda create -n genai python=3.10 -y

# Activate it
conda activate genai
```

---

## 📦 Step 4: Install Requirements

From inside the `intro-to-genai` folder:

```bash
pip install -r requirements.txt
```

---

## 📌 Step 5: Register Jupyter Kernel

So VS Code & Jupyter can see your environment:

```bash
python -m ipykernel install --user --name=genai --display-name "Python (genai)"
```

---

## 💻 Step 6: Open VS Code

Still in the same folder:

```bash
code .
```

This opens your `intro-to-genai` folder in VS Code.
Now when you open a `.ipynb` notebook → select kernel → Python (genai). ✅
