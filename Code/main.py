#We have 3 python files. In this file, main.py, we run the actual code and also the GUI. Functionality is imported from the other 2 files.
import Preprocessor
import Processor
import tkinter
from tkinter import *

questions, responses = Preprocessor.load_corpus()
#for debugging on terminal
print("Booting Up...")
question_list = Processor.vectorizer(questions)
print("The Chat Bot has loaded.")

window = tkinter.Tk()
#height is false so that we do not lose the fixed bar at the bottom
window.resizable(width=True, height=False)
window.title("Nova, the chatbot")
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
Nova = StringVar()
You = StringVar()
messages = Text(window, width=100, height=20, yscrollcommand=scrollbar.set, wrap=WORD)
messages.config(background="#008080")
scrollbar.config(command=messages.yview())
messages.pack(anchor='nw', expand=1, fill=BOTH)


def event_enter(key):
    Enter_pressed()


def Enter_pressed():

    input_get = You.get()
    messages.insert(END, "You: " + '%s\n' % input_get)
    #this gets the response from the Processor.py file and then prints them out
    get_response = Processor.process(input_get, question_list, responses)
    messages.insert(END, "Nova: " + '%s\n' % get_response)
    You.set('')
    messages.see(END)
    return "break"

Label(window, text=" user : ").pack(side=LEFT)
Entry(window, textvariable=You, width=10, background="white").pack(side=LEFT, anchor='nw', expand=1, fill=BOTH)
frame = Frame(window)
Button(window, width=10, text="Send", foreground="Black", command=Enter_pressed, relief="flat").pack(side=LEFT)
messages.insert(END, "Nova: " + '%s\n' % "Hello. My name is Nova, the astronomy Chat Bot. Pleased to meet you.")
window.bind("<Return>", event_enter)
frame.pack(anchor='nw', expand=1, fill=BOTH)
window.mainloop()






