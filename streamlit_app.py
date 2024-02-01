import streamlit as st
import requests
import json
import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Leer el archivo de audio

    try:
        text = recognizer.recognize_google(audio_data, language='es')  # Reconocer el audio
        return text
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return "Error al solicitar la transcripción; {0}".format(e)

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

# Subida de archivo de audio
audio_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])

# Botón para iniciar el proceso de transcripción y ordenación
if st.button("Generar autobiografía"):
    if audio_file is not None:
        st.write("Transcribiendo notas de voz...")
        audio_text = transcribe_audio(audio_file)
        st.write("Texto transcrito:")
        st.write(audio_text)

        st.write("Generando autobiografía...")
        autobiography = transcribe_and_order_notes(audio_text)
        st.write("Autobiografía generada:")
        st.write(autobiography)
    else:
        st.write("Por favor, carga un archivo de audio para generar la autobiografía.")
