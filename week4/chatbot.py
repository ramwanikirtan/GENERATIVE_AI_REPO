## 1. imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
## 2. initialize the model
model = ChatOpenAI()

chatHistory= []

## 3. create a simple terminal based bot
#run an infinite loop to take user input and generate responses until user types 'exit'
print("Welcome to the Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("user:")
    chatHistory.append(user_input)
    if user_input.lower()=="exit":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chatHistory)
    chatHistory.append(response.content)
    print("bot:", response.content)



print(chatHistory)
### This is a simple terminal based bot using langchain and openai
### but the problem is that there is no context awareness in this bot
### we will now add the context awareness to this bot
