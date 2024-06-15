#Installed Mysql on my computer
# link to mysql official installer
# pip install mysql (for fresh installation i needed to run the command below)
# opt command : sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
# pip install mysql-connector
# pip install mysql-connector-python 



import mysql.connector

dataBase = mysql.connector.connect(
    user = 'root',
    passwd = 'root',
    host = 'localhost',
    auth_plugin='mysql_native_password')

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("DB Init Done !")