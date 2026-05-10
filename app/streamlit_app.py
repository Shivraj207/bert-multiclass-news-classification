import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_news_category

st.set_page_config(page_title="BERT News Classifier", layout="centered")

st.title("BERT News Classification")
st.write("Classify news into World, Sports, Business, or Sci/Tech")

# Input box
user_input = st.text_area("Enter News Text:")

# Example buttons
st.write("### Try Examples:")
col1, col2 = st.columns(2)

sports_text = "Virat Kohli scored a century as India defeated Australia in the ICC Cricket World Cup final."
tech_text = "Google launched a new artificial intelligence model with advanced reasoning capabilities."

with col1:
    if st.button("⚽ Sports Example"):
        st.write(sports_text)
        print(sports_text)
        

with col2:
    if st.button("⚽ Tech Example"):
        st.write(tech_text)
        print(tech_text)
        
# Prediction
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            result, confidence = predict_news_category(user_input)

        # Colored output
        if result == "World":
            st.info(f"🌍 {result}")
        elif result == "Sports":
            st.success(f"⚽ {result}")
        elif result == "Business":
            st.warning(f"💼 {result}")
        else:
            st.write(f"🧪 {result}")

        st.write(f"Confidence: {confidence:.2f}")