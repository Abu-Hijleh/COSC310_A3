import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

#Preprocessor has functions to load the corpus questions and responses, as well as to format the user input so it can be used by the Processor file.

def load_corpus():  # Loads questions and responses from corpus.txt
    questions = []
    responses = []
    with open('Corpus.txt') as corpus:  # open corpus.txt
        for line in corpus.readlines():
            split = line.split("||")  # split lines into questions and responses then add to respective list
            questions.append(split[0])
            responses.append(split[1])
    return questions, responses


def sentence_formatter(sentence):  # Removes punctuation from sentence
    formatted_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    formatted_sentence = formatted_sentence.lower()
    return formatted_sentence


def sentence_lemmatizer(sentence):  # Changes words in the sentence to their root form
    lemmatized_word_bank = []
    lemmatizer = WordNetLemmatizer()
    split = sentence.split()
    for word in split:
        lemmatized_word_bank.append(lemmatizer.lemmatize(word))  # add lemmatized words to list
    lemmatized_sentence = ' '.join(lemmatized_word_bank)  # rejoin words into a sentence format
    return lemmatized_sentence


def sentence_cleaner(sentence):  # Removes stop words such as 'the', 'a' and 'in' from sentence
    tokens = word_tokenize(sentence)
    cleaned_tokens = [word for word in tokens if not word in stopwords.words()]  # Only add words that are not stopwords
    cleaned_sentence = ' '.join(cleaned_tokens)  # rejoin words into sentence format
    return cleaned_sentence
