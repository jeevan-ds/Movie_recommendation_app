

import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API'))

# MOvie Recomendation System
st.title("🍿🎥✮⋆Movie Recomendation System 🍿🎥✮⋆ ")

user_input=st.text_input("Enter the Movie Name")
submit=st.button("Click here.....")


model = genai.GenerativeModel('gemini-2.5-flash-lite')
if submit and user_input.strip():
    st.markdown(f'Movie name entered:{user_input}')
    response=model.generate_content(f'Generate movie Recommendations related to:{user_input}')
    st.write(f'Related Recommendations for similar movies:\n {response.text}')
else:
    st.write(f"Enter a movie name")