from fastapi import FastAPI, File, UploadFile
import pandas as pd
import joblib
import uvicorn
from preprocessing import preprocessing_pipeline  
import numpy as np
app = FastAPI()

# Ruta del modelo
model_path = "./model/final_model_parte2.pkl"

# Cargar modelo
with open(model_path, 'rb') as model_file:
    final_model = joblib.load(model_file)

@app.get("/")
def read_root():
    return {
        "description": "API para realizar predicciones desde un archivo CSV.",
        "instructions": "Sube un archivo CSV con las características necesarias para realizar predicciones."
    }

@app.post("/predict/")
def predict_from_file(file: UploadFile = File(...)):
    """
    Endpoint para realizar predicciones desde un archivo CSV.

    Parámetros:
    - file: Archivo CSV subido por el usuario.

    Retorna:
    - Predicciones realizadas por el modelo sobre los datos del archivo.
    """
    try:
        # Leer el archivo CSV cargado
        predict_data = pd.read_csv(file.file)
        print(predict_data.head())

        # Verificar si el archivo contiene datos
        if predict_data.empty:
            return {"error": "El archivo CSV está vacío."}

        # Transformar los datos usando el pipeline importado
        predict_data_transformed = preprocessing_pipeline.transform(predict_data)

        # Realizar la predicción
        predictions = final_model.predict_proba(predict_data_transformed)

        # Retornar las predicciones
        return {"predictions": predictions.tolist()}

    except Exception as e:
        return {"error": f"Ocurrió un error procesando el archivo: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

