import spacy
from scraper import scrape_pccoe

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# Placeholder for storing website data
pccoe_data = scrape_pccoe()

def generate_response(query):
    doc = nlp(query.lower())

    if "admission" in query:
        return pccoe_data.get("admissions", "Sorry, I couldn't find information on admissions.")
    elif "scholarship" in query:
        return pccoe_data.get("scholarships", "Sorry, I couldn't find information on scholarships.")
    elif "course" in query:
        return pccoe_data.get("courses", "Sorry, I couldn't find information on courses.")
    else:
        return "I'm sorry, I don't understand your question. Could you please rephrase it?"
