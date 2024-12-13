import gradio as gr
import requests
import pandas as pd
import numpy as np

def predict(csv_file):
    """
    Función para enviar el archivo CSV al backend FastAPI y recibir las predicciones.

    Parámetros:
    - csv_file: Archivo CSV subido desde Gradio.

    Retorna:
    - Respuesta del backend con las predicciones.
    """
    # URL de la API
    url = "http://127.0.0.1:8000/predict/"

    # Abrir el archivo y enviarlo como parte de la solicitud
    with open(csv_file.name, "rb") as f:
        files = {"file": (csv_file.name, f, "text/csv")}
        response = requests.post(url, files=files)

    # Verificar la respuesta de la API
    if response.status_code == 200:
        result = response.json()
        if "predictions" in result:
            # Convertir predicciones a un DataFrame para mejor visualización
            df = pd.DataFrame(result["predictions"], columns=["Probabilidad Clase 0", "Probabilidad Clase 1"])
            return df
        elif "error" in result:
            return f"Error: {result['error']}"
    else:
        return f"Error en la solicitud: {response.status_code}"

# Configurar la interfaz de Gradio
input_csv = gr.File(label="Sube un archivo CSV con los datos para predecir")
output_predictions = gr.Dataframe(label="Predicciones")

description = "Sube un archivo CSV para realizar predicciones utilizando el modelo cargado en el backend."

gr.Interface(
    fn=predict,
    inputs=input_csv,
    outputs=output_predictions,
    title="Interfaz de Predicción",
    description=description,
    
).launch(share=True)