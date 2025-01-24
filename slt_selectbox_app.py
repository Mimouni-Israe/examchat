import streamlit as st

st.header('st.selectbox')

# Question et choix des modèles
option = st.selectbox(
     'Choisissez un modèle :',
     ('gpt-3.5-turbo', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-1106', 'gpt-3.5-turbo-0125')
)

# Afficher le modèle sélectionné
st.write('Vous avez choisi le modèle :', option)