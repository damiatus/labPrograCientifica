import gradio as gr
import requests

def make_prediction(file, manual_inputs):
    """
    Realiza la predicción conectándose al backend de FastAPI.
    """
    url = "http://localhost:8000/predict/"  # Cambia la URL según la configuración

    if file is not None:
        response = requests.post(url, files={"file": file})
    elif manual_inputs:
        response = requests.post(url, data=manual_inputs)
    else:
        return "Debe proporcionar un archivo o datos manuales."

    if response.status_code == 200:
        return response.json()
    else:
        return response.json().get("message", "Error en la predicción.")

# Interfaz Gradio
file_input = gr.File(label="Cargar archivo CSV", type="file")
manual_inputs = gr.Textbox(label="Ingrese datos manuales (formato JSON)")

iface = gr.Interface(
    fn=make_prediction,
    inputs=[file_input, manual_inputs],
    outputs=["json"],
    title="App de Predicción",
    description="Cargue un archivo CSV o introduzca los datos manualmente para obtener predicciones."
)

iface.launch()

