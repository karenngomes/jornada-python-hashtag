# pip install openai streamlit python-dotenv
# streamlit run main.py

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

st.write("# Chatbot com IA") # markdown

if not "messages_list" in st.session_state:
    st.session_state["messages_list"] = []

user_text = st.chat_input("Digite sua mensagem")

for message in st.session_state["messages_list"]:
    st.chat_message(message["role"]).write(message["content"])

if (user_text):
    st.chat_message("user").write(user_text)
    user_message = {"role": "user", "content": user_text}
    st.session_state["messages_list"].append(user_message)

    ai_response = client.chat.completions.create(
        messages=st.session_state["messages_list"],
        model="gpt-4o"
    )

    ai_response_text = ai_response.choices[0].message.content

    st.chat_message("assistant").write(ai_response_text)

    ai_message = {"role": "assistant", "content": ai_response_text}
    st.session_state["messages_list"].append(ai_message)