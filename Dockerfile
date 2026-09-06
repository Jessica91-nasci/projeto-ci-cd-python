# Usa uma imagem oficial do Python (versao leve)
FROM python:3.10-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos da sua pasta atual para dentro do container
COPY . /app

# Comando que o container vai executar ao ligar
CMD ["python", "main.py"]
