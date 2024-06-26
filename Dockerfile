# Utilise une image de base Python officielle
FROM python:3.12-slim

# Installer les paquets nécessaires pour MySQL et les outils de construction
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Supprimer les paquets de build pour réduire la taille de l'image
RUN apt-get purge -y \
    build-essential \
    pkg-config && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copier tout le contenu du projet dans le répertoire de travail
COPY . /app/

# Copier wait-for-it.sh dans le répertoire de travail
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copier le script d'initialisation de la base de données
COPY mydb.py /app/mydb.py

# Exposer le port 8000 pour l'application Django
EXPOSE 8000

# Définir la commande par défaut pour exécuter le serveur Django
CMD ["./wait-for-it.sh", "db:3306", "--", "bash", "-c", "python init_db.py && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]