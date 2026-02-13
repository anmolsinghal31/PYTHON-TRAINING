import mysql.connector
host="localhost"
user="root"
password="Anmol@123"
database="feb2026"

connection = mysql.connector.connect(
  host = host,
  user = user,
  password = password,
  database = database
)

cursor = connection.cursor()
print("connected to the database successfully")

query="SELECT * FROM employee"
cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)
