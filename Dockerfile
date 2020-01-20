############################################################
# Dockerfile Python - Flask
############################################################
FROM python:3

# Información de Metadata
LABEL "com.antonioalfa22.apirest"="apirest"
LABEL maintainer="antonioalfa22@gmail.com"
LABEL version="1.0"

# Crear directorio de trabajo
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . .

# Install requirements
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python server.py run