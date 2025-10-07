## 1. imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

## 2. initialize the model
model = ChatOpenAI()


## 3. create a simple terminal based bot
#run an infinite loop to take user input and generate responses until user types 'exit'
print("Welcome to the Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("user: ")
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(user_input)
    print("bot:", response.content)


