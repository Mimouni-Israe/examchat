import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
     # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            max_tokens = 200,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st

st.header('st.selectbox')

# Question et choix des modèles
option = st.selectbox(
     'Choisissez un modèle :',
     ('gpt-3.5-turbo', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-1106', 'gpt-3.5-turbo-0125')
)

# Afficher le modèle sélectionné
st.write('Vous avez choisi le modèle :', option)

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Nouveau slider pour choisir une valeur entre 0 et 500
st.subheader('Choisir la valeur de max_tokens')

max_tokens = st.slider(
    'Sélectionnez une valeur pour max_tokens :',
    0, 500, 100  # Min = 0, Max = 500, Valeur par défaut = 100
)

# Afficher la valeur choisie
st.write("La valeur de max_tokens est :", max_tokens)