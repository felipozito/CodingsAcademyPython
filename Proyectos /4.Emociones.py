# Instalar dependencias: pip install requests googletrans==4.0.0-rc1 streamlit matplotlib

import requests
from googletrans import Translator
import streamlit as st
import matplotlib.pyplot as plt

def analizar_emocion(texto):
    API_URL = "https://api-inference.huggingface.co/models/finiteautomata/beto-emotion-analysis"
    headers = {"Authorization": "Bearer TU_API_KEY"}  # Obtén una key gratis en Hugging Face
    response = requests.post(API_URL, headers=headers, json={"inputs": texto})
    return response.json()[0][0]['label']

def traducir_con_emocion(texto, idioma="en"):
    emocion = analizar_emocion(texto)
    traductor = Translator()
    traduccion = traductor.translate(texto, dest=idioma).text
    emociones_a_emojis = {"joy": " 😊", "anger": " 😠", "sadness": " 😢"}
    return traduccion + emociones_a_emojis.get(emocion, "")

# Interfaz
st.title("🔍 Traductor de Emociones")
texto = st.text_area("Ingresa tu texto:")
idioma = st.selectbox("Idioma destino", ["en", "fr", "ja", "de"])

if st.button("Traducir"):
    resultado = traducir_con_emocion(texto, idioma)
    st.success(f"Traducción: {resultado}")
    emocion = analizar_emocion(texto)
    fig, ax = plt.subplots()
    ax.bar(["Emoción"], [1], color="skyblue")
    ax.set_title(f"Emoción detectada: {emocion}")
    st.pyplot(fig)