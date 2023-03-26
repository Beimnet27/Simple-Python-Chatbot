# Import the libraries

import nltk
from nltk.chat.util import Chat, reflections

# Define the responses

pairs = [
    ['hi', ['Hello!', 'Hi there!']],
    ['what is your name', ['My name is Chatbot', 'I am Chatbot']],
    ['how are you', ['I am doing well', 'I am fine, thanks']],
    
    ['bye', ['Goodbye', 'See you later']],
]

# Create the chatbot

chatbot = Chat(pairs, reflections)

# Define the function for the dialogue loop

def eg_input():
    text = input("You: ")
    if text.lower() == 'quit':
        print("Chatbot: Goodbye")
        return
    response = chatbot.respond(text)
    print("Chatbot: ", response)
    eg_input()

# Call the dialogue loop function

eg_input()
