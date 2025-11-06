# Imagen base oficial de Python (puedes usar otra versión si lo deseas)
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias primero
COPY src/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta src
COPY src/ .

# Comando por defecto para ejecutar tu aplicación
CMD ["python", "main.py"]
