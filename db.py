import MySQLdb
import mysql.connector

mydb = MySQLdb.connect(host="34.102.69.250", user="root", passwd="1234")

mycursor = mydb.cursor()

mycursor.execute("show databases")

for x in mycursor:
    print(x)

