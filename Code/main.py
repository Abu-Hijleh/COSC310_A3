import Preprocessor
import Processor

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
