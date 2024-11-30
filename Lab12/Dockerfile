# Usa una imagen base de Python (versión 3.10, por ejemplo)
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las dependencias usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto que utilizará tu aplicación (por ejemplo, 8000 para FastAPI)
EXPOSE 8000

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]
