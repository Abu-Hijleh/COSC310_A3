import Preprocessor
import Processor
import sys, os


def blockPrint():  # Remove all the printing onto console when chatbot is loading
    sys.stdout = open(os.devnull, 'w')


def enablePrint():  # Restores printing
    sys.stdout = sys.__stdout__


questions, responses = Preprocessor.load_corpus()

print("Booting Up...")
blockPrint()
question_list = Processor.vectorizer(questions)
enablePrint()
print("The Chat Bot has loaded. Type 'goodbye' to exit")
print("Hello. My name is Nova, the astronomy and geography Chat Bot. Pleased to meet you")

while True:  # The Chat Bot will run until 'goodbye' is inputted
    user_input = input("Input: ").lower()
    if user_input.lower() == "goodbye":
        print("Nova: See you soon!")
        quit()
    else:
        print("Nova:", end=' ')
        Processor.process(user_input, question_list, responses)
