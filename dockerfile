# Use uma imagem base leve de Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências de sistema básicas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos primeiro (otimiza o cache do Docker)
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto para o container
COPY . .

# Expõe as portas que você definiu no compose
EXPOSE 8501
EXPOSE 8000

# O comando final é sobrescrito pelo 'command' do seu docker-compose.yml,
# então não precisamos de um CMD rígido aqui.