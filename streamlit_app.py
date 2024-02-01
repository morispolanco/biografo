import streamlit as st
import requests
import json

# Función para corregir texto utilizando la API
def corregir_texto(texto):
    # URL de la API
    url = "https://api.respell.ai/v1/run"
    
    # Cuerpo de la solicitud
    payload = {
        "spellId": "dN5cL9gF7TOXGpQHIxkeb",
        "spellVersionId": "QvIqkK5I7fhzvQfqJ6oOr",
        "inputs": {
            "input": texto,
        }
    }

    # Cabeceras de la solicitud
    headers = {
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        texto_corregido = data["outputs"]["output"]
        return texto_corregido
    else:
        return "Error al corregir el texto. Por favor, inténtalo de nuevo más tarde."

# Configuración de la aplicación Streamlit
st.title("Corrección de Texto")

# Área de entrada de texto
texto_usuario = st.text_area("Ingresa el texto que quieres corregir")

# Botón para corregir el texto
if st.button("Corregir"):
    if texto_usuario:
        texto_corregido = corregir_texto(texto_usuario)
        st.subheader("Texto Corregido")
        st.write(texto_corregido)
    else:
        st.warning("Por favor, ingresa texto para corregir")
