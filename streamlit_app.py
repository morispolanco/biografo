import streamlit as st
import requests
import json

def transcribe_and_order_notes(notes):
    # Llamada a la API para transcribir notas
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # Esta es tu clave de API
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": "EvBQVBWF4tRxbbJFc3ULR",
            # Este campo se puede omitir para ejecutar la última versión publicada
            "spellVersionId": "qz5t6E9DnzKAsW-9UiHtU",
            # Rellenar un valor para tu bloque de entrada dinámica
            "inputs": {
                "input": notes,
            }
        }),
    )

    # Manejar la respuesta de la API
    if response.status_code == 200:
        data = response.json()
        if "output" in data:
            return data["output"]
    return "Error al transcribir las notas"

# Configuración de la aplicación Streamlit
st.title("Transcripción de notas de voz y autobiografía")

# Entrada de texto para las notas de voz
notes_input = st.text_area("Ingresa tus notas de voz aquí:")

# Botón para iniciar el proceso de transcripción y ordenación
if st.button("Generar autobiografía"):
    if notes_input:
        st.write("Transcribiendo y ordenando notas...")
        autobiography = transcribe_and_order_notes(notes_input)
        st.write("Autobiografía generada:")
        st.write(autobiography)
    else:
        st.write("Por favor, ingresa algunas notas de voz para generar la autobiografía.")
