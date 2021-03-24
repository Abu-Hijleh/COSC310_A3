import Preprocessor
import Processor
from tkinter import *
root = Tk()
root.title("Nova")
root.resizable(width=FALSE,height=FALSE)
root.geometry("400x500")
messages = Text(root, bd=1, bg="#008080",width="50",height="8",font=("Arial",16),foreground="#000000")
messages.place(x=0, y=0, height = 500, width = 500 )

input = Text(root, bd=0, bg="white",width="30", height="4", font=("Arial", 16), foreground="#000000")
input.place(x=100, y=400, height=80, width=300)

scrollbar = Scrollbar(root, command=messages.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

Button= Button(root, text="Send",  width="10", height=6,
                    bd=0, bg="#7B0C0C", activebackground="#B7312A",foreground="black",font=("Arial", 12))
Button.place(x=0, y=400, height=80)

root.mainloop()
#testing branching
#We have 3 python files. In this file, main.py, we run the actual code. Functionality is imported from the other 2 files.

questions, responses = Preprocessor.load_corpus()

print("Booting Up...")
question_list = Processor.vectorizer(questions)
print("The Chat Bot has loaded. Type 'goodbye' to exit")
print("Hello. My name is Nova, the astronomy Chat Bot. Pleased to meet you")

#while loop to terminate conversation
while True:  # The Chat Bot will run until 'goodbye' is inputted
    user_input = input("Input: ").lower()
    if user_input.lower() == "goodbye":
        print("Nova: See you soon!")
        quit()
    else:
        print("Nova:",end=' ')
        Processor.process(user_input, question_list, responses) #calls function from Processor file.
