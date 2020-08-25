import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="3Uw49FN_xSCX"
)

mycursor = mydb.cursor()

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    sql = "INSERT INTO lab2.wordcount (word, count) VALUES (%s, %s)"
    val = (word, count)
    mycursor.execute(sql, val)

mydb.commit()
mycursor.close()
mydb.close()
