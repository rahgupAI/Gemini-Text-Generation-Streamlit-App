from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

# UI improvements
st.set_page_config(
    page_title="Ask Gemini!",
    layout="wide",  # Wider layout for better use of space
    initial_sidebar_state="collapsed",  # Hide sidebar initially
)

st.title("Talk to Gemini")  # Clear and descriptive title

user_input = st.text_input(
    "Ask your question:", key="user_input", placeholder="Type your question here..."
)  # Descriptive placeholder text

if user_input:
    st.subheader("Gemini's Response:")
    response = get_gemini_response(user_input)
    st.write(response)
    st.success("Got your response! Ask another question or refresh the page for a new start.")
else:
    st.info("Start a conversation by entering your question in the box above.")
