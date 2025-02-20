import re 
import spacy
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")

def extract_keywords_tfidf(text):
    """Extract keywords from text using TF-IDF"""
    vectorizer = TfidfVectorizer(stop_words="english", max_features=10)
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)

def extract_entities_spacy(text):
    """Extract key entities like skills, job title using spacy"""
    doc = nlp(text)
    skills = []
    job_title = []

    for ent in doc.ents:
        if ent.label_ in ["ORG","PERSON","GPE"]:
            continue
        if ent.label_ in ["JOB_TITLE","WORK_OF_ART"]:
            job_title.append(ent.text)
        else:
            skills.append(ent.text)
    
    return {
        "job_titles": list(set(job_title)),
        "skills": list(set(skills))
    }

def extract_experience_level(text):
    """Extract experience level from text"""
    exp_pattern = r"\b(Entry level|Mid level|Junior|Senior level|Executive level|Associate)\b"
    matches = re.findall(exp_pattern, text, re.IGNORECASE)
    return list(set(matches))

def parse_job_description(text):
    """"Main function to parse job description"""
    keywords = extract_keywords_tfidf(text)
    entities = extract_entities_spacy(text)
    experience_level = extract_experience_level(text)

    return {
        "keywords": keywords,
        "entities": entities,
        "experience_level": experience_level
    }