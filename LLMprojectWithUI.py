import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Welcome to the First Project")
st.subheader("Made by @Rik")

name = st.text_input("Enter your name here:")

if st.button("Submit"):
    st.write(f"Hello, {name}!")

mood = st.selectbox("Pick your current mood:", ['happy', 'sad', 'tired', 'motivated'])

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational"
)

model = ChatHuggingFace(llm=llm, temperature=0.9, max_tokens=100)

prompt_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a Mood-Based Motivational Speaker.'),
    ('human', 'Write a motivational quote for {name} based on this mood: {mood}.')
])

if st.button("Get My Quote"):
    if not name:
        st.warning("Please enter your name first.")
    else:
        prompt = prompt_template.format_messages(name=name, mood=mood)
        response = model.invoke(prompt)
        st.write(response.content)
