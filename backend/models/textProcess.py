import spacy
import nltk 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Downloading essential nltk data
nltk.download('stopwords') # removal of and, this, is
nltk.download('punkt') # tokenization

# load spacy model 
nlp = spacy.load('en_core_web_sm') # extract job related entities


