# Customer Satisfaction Analysis with Natural Language Processing

# Libraries

import streamlit as st    # Implementation of the Predictive Machine
import nltk               # Natural Language Tool Kit

# Criação do Sistema

st.write("# Customer Satisfaction Analysis")                      # System Title
user_input = st.text_input("Rate our service: ")                  # Data input


# Creation of the PM/NLP

nltk.download("vader_lexicon")     # Input data for training

from nltk.sentiment.vader import SentimentIntensityAnalyzer 
s = SentimentIntensityAnalyzer()        # Predictive Machine

score = s.polarity_scores(user_input)   # Evaluates the input

if score == 0:                          # Classify the input
    st.write("")
elif score['neg'] != 0:
    st.write("Negative Review")
elif score['pos'] != 0:
    st.write("Positive Review")
