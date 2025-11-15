# Image Python légère
FROM python:3.9-slim

# Installation de netcat pour vérifier la connexion MySQL
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie du code source
COPY . .

# Rendre le script d'entrée exécutable
RUN chmod +x entrypoint.sh

# Port exposé par l'application Flask
EXPOSE 5000

# Commande de démarrage avec initialisation de la DB
CMD ["./entrypoint.sh"]