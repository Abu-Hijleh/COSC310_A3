# NOVABOT, THE ROBOT ASTRONOMER AND GEOGRAPHER
---

# Project Description

Nova is a chatbot that is passionate about teaching astronomy and geography to users. Her implementation of natural language processing in python allows her to understand and answer user questions related to astronomy such as stars, galaxies, black holes and planets, and questions related to geography such as country capitals and geographical records. She was created with the intent to spread basic knowledge about astronomy and geography to individuals who are interested in these fields. 

# Software Development Life Cycle

We chose to use the incremental development life cycle. This life cycle is ideal because we would like to continuously gather user feedback and make corrective changes throughout development. As part of the agile process, we will also be participating in peer programming since we all have limited experience creating chatbots and want to support each other. Our incremental life cycle will include a project planning phase, a researching phase, a development phase, a review phase and then a presentation phase. We aim to develop a basic chatbot in the first major increment then develop a GUI for the chatbot in the second major increment. 

# How does Nova work?

Nova was developed in python and uses natural language processing to understand and converse with the user. She takes the input from the user and cleans the sentences into a condensed and easily-readable format. She then compares the input to the questions she has in her questionbank and gives a response based on the similarity between the input and questionbank questions. All the questions and responses are found inside the corpus.txt file and may be expanded or changed as more astronomy or geography questions are thought of. 

# Requirements

You will need to download and install NLTK and Spacy in your python IDE before using Nova. You will also need to download en_core_web_lg for Spacy. Once that is complete, you can run main.py and begin using Nova. 

- `pip install nltk`
- `pip install -U spacy`
- `python -m spacy download en_core_web_lg`
- `pip install pyspellchecker`

# Sections

- **Corpus**: Contains a compilation of questions and responses that Nova uses to converse with the user
- **Preprocessor**: This section is in charge of formatting the user input into a more readable format for the system
- **Processor**: This section takes the preprocessed data and tries to match it with its accurate response
- **Main**: This section introduces the user, take their input and manages how the program executes 
- **norm_punc**: This section was taken from the Phrasal library. It normalizes sentences by removing elements such as special characters, extra spaces and apostrophes. 

`Corpus` --> `Preprocessor` --> `Processor` --> `Main`

# Capabilities

- Nova utilizes natural language processing and pattern matching effectively so the user input does not have to match the predefined questions exactly to get an accurate response
  - `Input: what is nuclear fusion?`
  - `Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium`
  - `Input: nuclear fusion`
  - `Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium`
  - `Input: what is the capital of Canada?'
  - `Nova: Ottowa`
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
- Nova recognizes synonyms of the word "bye" and uses them to find out when the user is done asking questions

# Limitations

- Nova can take a while to process user input and output the correct responses since there is a lot of conversion and formatting to be done. The processing time could be lowered by using more efficient functions.
- Nova is somewhat limited to the predefined questions and responses in the corpus.txt. The corpus.txt will have to be expanded to allow Nova to answer more questions.
  - `Input: what is a megabyte?`
  - `Nova: I do not understand your question`
