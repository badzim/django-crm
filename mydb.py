#Installed Mysql on my computer
# link to mysql official installer
# pip install mysql (for fresh installation i needed to run the command below)
# opt command : sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
# pip install mysql-connector
# pip install mysql-connector-python 



import mysql.connector
import time

# Attendre que le serveur MySQL soit prêt
time.sleep(10)

dataBase = mysql.connector.connect(
    user='root',
    passwd='root',
    host='localhost',
)

# Préparer un objet curseur
cursorObject = dataBase.cursor()

# Vérifier si la base de données existe
cursorObject.execute("SHOW DATABASES LIKE 'elderco'")
database_exists = cursorObject.fetchone()

# Créer la base de données si elle n'existe pas
if not database_exists:
    cursorObject.execute("CREATE DATABASE elderco")
    print("DB Init Done !")
else:
    print("Database already exists")

cursorObject.close()
dataBase.close()
