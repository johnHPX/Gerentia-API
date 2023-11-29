# Use a imagem oficial do Python como base
FROM python:3.10

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . .

# Expõe a porta em que a aplicação estará em execução
EXPOSE 8000

# Define a variável de ambiente para o Flask saber que está em um ambiente de produção
ENV FLASK_ENV=production 

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["python", "main.py"]
