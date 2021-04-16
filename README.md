# NOVABOT, THE ROBOT ASTRONOMER AND GEOGRAPHER
---

# Project Description

Nova is a chatbot that is passionate about teaching astronomy and geography to users. Her implementation of natural language processing in python allows her to understand and answer user questions related to astronomy such as stars, galaxies, black holes and planets, and questions related to geography such as country capitals and geographical records. She was created with the intent to spread basic knowledge about astronomy and geography to individuals who are interested in these fields. 

# How does Nova work?

Nova was developed in python and uses natural language processing to understand and converse with the user. She takes the input from the user and cleans the sentences into a condensed and easily-readable format. She then compares the input to the questions she has in her questionbank and gives a response based on the similarity between the input and questionbank questions. All the questions and responses are found inside the corpus.txt file and may be expanded or changed as more astronomy or geography questions are thought of. 

# Installations

- `pip install nltk`
- `pip install -U spacy`
- `python -m spacy download en_core_web_lg`
- `pip install pyspellchecker`
- `pip install google-cloud-translate==2.0.1`
- `pip install beautifulsoup4`


# Files

- **Corpus**: Contains a compilation of questions and responses that Nova uses to converse with the user
- **Preprocessor**: This file is in charge of formatting the user input into a more readable format for the system
- **Processor**: This file takes the preprocessed data and tries to match it with its accurate response
- **Main**: This file introduces the user, takes their input, generates the GUI, and manages how the program executes 
- **norm_punc**: This file was taken from the Phrasal library. It normalizes sentences by removing elements such as special characters, extra spaces and apostrophes. 
- **APIs**: This file includes the Wikipedia and Google Translate APIs that were added as part of individual assigment submission. 

# New Features
-Google Translate:Accepts and replies to questions in languages other than english in order to make information more accessable. 
- Wikipedia API: If the user asks a question in english that Nova does not recognize, the question is sent to the method that uses the wikepedia API in order to attempt to generate a response. 
# Capabilities

- Nova utilizes natural language processing and pattern matching effectively so the user input does not have to match the predefined questions exactly to get an accurate response
  - `Input: what is nuclear fusion?`
  - `Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium`
  - `Input: nuclear fusion`
  - `Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium`
  - `Input: what is the capital of Canada?'
  - `Nova: Ottawa`
- Nova cover a wide range of topics in astronomy, astrophysics and geography
- Nova is easy to refactor and reuse since its structure is very basic. The corpus.txt can be modified to suit any topic of interest
- Nova can recognize inputs even if they have simple spelling errors
  - `Input: what s the capitall pf jamaica?`
  - `Nova: Kingston`
- Nova can recognize user inputs even if they contain special characters 
  - `Input: what i$ the c@pital of India?`
  - `Nova: New Delhi`
- Nova can recognize the parts of speech of words in the user input
  - `Input: what is a white dwarf?`
  - `Nova: Parts of Speech:  [('white', 'JJ'), ('dwarf', 'NN')]`
- Nove can respond to questions in many languages 
- Nova can use the Wikipedia API if to search for answers to questions she does not understand

# Limitations

- Nova can take a while to process user input and output the correct responses since there is a lot of conversion and formatting to be done. The processing time could be lowered by using more efficient functions.

