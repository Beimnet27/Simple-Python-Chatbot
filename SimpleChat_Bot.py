# Import the libraries
import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import *

# Define the responses
pairs = [
    ['hi', ['Hello!', 'Hi there!']],
    ['what is your name', ['My name is Chatbot', 'I am Chatbot']],
    ['how are you', ['I am doing well', 'I am fine, thanks']],
    ['bye', ['Goodbye', 'See you later']],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Create the user interface
def send():
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)
    if msg != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot.respond(msg)
        ChatLog.insert(END, "Chatbot: " + res + "\n\n")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

ChatLog = Text(root, bd=0, bg="purple", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(root, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send)

EntryBox = Text(root, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=60, width=265)
SendButton.place(x=6, y=401, height=60)

root.mainloop()
