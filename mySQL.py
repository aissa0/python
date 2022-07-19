import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="aliissa",
  password="AliIssa@2233",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Students (name VARCHAR(255), address INTEGER(10))")