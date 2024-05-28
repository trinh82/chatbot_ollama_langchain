import streamlit as st
from langchain_community.llms import Ollama

# initialize an Ollama's LLM (llama2, llama3, mistral,...)
llm = Ollama(model='llama2:latest')

# create user interface using streamlit library
st.title('Chatbot using LLM locally')

prompt = st.text_area("Enter your question:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write_stream(llm.stream(prompt,stop = ['<|eot_id|>']))

