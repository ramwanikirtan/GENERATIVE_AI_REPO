## taking input from user and sending it to the model


#1. imports

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

#2. initialize the model
model = ChatOpenAI()

#3. create the UI
st.header("Prompt UI") 


user_input = st.text_input("Enter your prompt here")  ### TAKING INPUT FROM USER
if st.button("Submit"):     ### WHEN USER CLICKS ON SUBMIT BUTTON
    st.write("generating response...")
    response = model.invoke(user_input)
    st.write(response.content)