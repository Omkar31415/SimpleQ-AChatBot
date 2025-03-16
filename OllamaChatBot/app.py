import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")

## Select the OpenAI model
engine=st.sidebar.selectbox("Select Open Source model",["mistral",'gemma2','gemma:2b'])

## Main interface for user input
st.write("Go ahead and ask any question!")
user_input=st.text_input("You:")

if user_input :
    response=generate_response(user_input,engine)
    st.write(response)
else:
    st.write("Waiting for user...")


