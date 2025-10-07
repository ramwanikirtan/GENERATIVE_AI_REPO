# instead of one prompt we will create a dynamic prompt using PromptTemplate
# with three input variables
# and we will gave option to user to select the values of these input variables using dropdowns in streamlit
# and then we will send the final prompt to the model and get the response
# and display the response in the UI

#1. imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv  
load_dotenv()
import streamlit as st


#2. initialize the model
model = ChatOpenAI()

#3. create the ui
st.header("Research Paper Summarizer")

## dropdowns for input variables
paper_input = st.selectbox(
    "Select a research paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "ResNet: Deep Residual Learning for Image Recognition"])


style_input = st.selectbox(
    "Select explanation style", ["Technical", "Layman", "Analogy-based", "Step-by-step", "Code snippets","mathematical"])

length_input = st.selectbox(
    "Select explanation length", ["Brief", "Detailed", "Concise", "In-depth", "Summary"])

## create the prompt template

template = load_prompt("research_paper_summarizer.json")  ## see how much easier it is to load the prompt from json file



## get the final prompt by filling the input variables in the template
final_prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    }
)

## send the final prompt to the model and get the response

if st.button("Submit"):
    st.write("generating response...")
    response = model.invoke(final_prompt)
    st.write(response.content)