import streamlit as st
import requests
import json

# Función para llamar a la API y corregir el texto
def corregir_texto(texto):
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # This is your API key
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": "EvBQVBWF4tRxbbJFc3ULR",
            # This field can be omitted to run the latest published version
            "spellVersionId": "qz5t6E9DnzKAsW-9UiHtU",
            # Fill in a value for your dynamic input block
            "inputs": {
                "input": texto,
            }
        }),
    )
    
    if response.status_code == 200:
        data = response.json()
        corrected_text = data.get("outputs", {}).get("output", "")
        return corrected_text
    else:
        return "Error al procesar el texto. Por favor, inténtalo de nuevo más tarde."

# Configuración de la aplicación de Streamlit
st.title("Corrección de Texto con respell.ai")

# Área de entrada de texto
texto_input = st.text_area("Introduce el texto que quieres corregir:")

# Botón para corregir el texto
if st.button("Corregir Texto"):
    if texto_input:
        texto_corregido = corregir_texto(texto_input)
        st.subheader("Texto Corregido:")
        st.write(texto_corregido)
    else:
        st.warning("Por favor, introduce texto para corregir.")
