# Utilise une image de base Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le répertoire de travail
COPY . /app/

# Exposer le port 8000 pour l'application Django
EXPOSE 8000

# Définir la commande par défaut pour exécuter le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
