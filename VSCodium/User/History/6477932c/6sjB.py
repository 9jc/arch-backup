
import mysql.connector

# try:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Passfx"
    )

cursor = mydb.cursor()
# except mysql.connector.Error as error:
    # print("Failed to connect to MySQL database: {}".format(error))

cursor.execute("CREATE DATABASE IF NOT EXISTS Passfx")
