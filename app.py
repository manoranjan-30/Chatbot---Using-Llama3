from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv 

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
##langsmith tracking
os.environ["LANGCHAIN_TRACKER_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## prompt template 

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you rare an helpful assistan. Please response to the queries"),
        ("user","question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))