## taking input from user and sending it to the model


#1. imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st



#2. initialize the model
model = ChatOpenAI()
#3. create the UI
 
st.header("Simple Chatbot")
user_input = st.text_input("Enter your message here:")

if st.button("Send"):
    response = model.invoke(user_input)
    st.text_area(response.content)




### THE ABOVE PROMPT IS STATIC WHICH IS NOT A GOOD PRACTICE FOR EFFECTIVE PROMPTING