import string
from spellchecker import SpellChecker
import norm_punc
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


# Preprocessor has functions to load the corpus questions and responses, as well as to format the user input so it can be used by the Processor file.

def load_corpus():  # Loads questions and responses from corpus.txt
    questions = []
    responses = []
    with open('Corpus.txt') as corpus:  # open corpus.txt
        for line in corpus.readlines():
            split = line.split("||")  # split lines into questions and responses then add to respective list
            questions.append(split[0])
            responses.append(split[1])
    return questions, responses


def sentence_normalizer(sentence): # Removes any special characters and emojis from the user input
    standard_char_list = "abcdefghijklmnopqrstuvwsyz- "
    temp_sentence = ""
    normalized_sentence = norm_punc.normalize_text(str(sentence.lower()),fix_encoding=True,strip_emojis=True)
    for char in normalized_sentence:
        for standardChar in standard_char_list:
            if standardChar == char:
                temp_sentence += char
                break
    return temp_sentence


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
    cleaned_tokens = token_spellchecker(cleaned_tokens)
    token_postagging(cleaned_tokens)
    token_synonyms(cleaned_tokens)
    cleaned_sentence = ' '.join(cleaned_tokens)  # rejoin words into sentence format
    return cleaned_sentence


def token_spellchecker(tokens): # Corrects any minor spelling errors in the user input
    spell = SpellChecker()
    correct_spelling = [spell.correction(word) for word in tokens]
    return correct_spelling


def token_postagging(tokens): # Tags the part of speech of the words in the user input
    print("Parts of Speech: ", nltk.pos_tag(tokens))


def token_synonyms(tokens): # Finds synonyms in the user input
    for word in tokens:
        print(wordnet.synsets(word))
