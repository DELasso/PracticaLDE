# Usa una imagen de Python
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Instalar dependencias si son necesarias (en este caso, no hay librerías externas)

# Ejecutar la aplicación
CMD ["python", "PracticaLDE2.py"]
