from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question."),
        ("user", "Question: {question}")
    ]
)

# Frontend using Streamlit
st.title("Aarsh's ChatGPT")

input_text = st.text_input("Enter your question here:")

# Ollama and LLM model integration
llm = Ollama(model="gemma2:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))