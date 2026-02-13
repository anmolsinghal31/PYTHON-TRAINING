import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anmol@123",
    database="feb2026"
)
cursor = connection.cursor()

# Task 1: Fetch
cursor.execute("SELECT * FROM employee WHERE Salary > 50000")
print("High Salary Employees:")
for row in cursor.fetchall():
    print(row)

# Task 2: Insert (Using 105 to avoid Duplicate Error)
sql_insert = "INSERT INTO employee (Employee_id, Employee_Name, Salary) VALUES (%s, %s, %s)"
val_insert = (105, "Rahul", 60000)
cursor.execute(sql_insert, val_insert)
connection.commit()
print("New employee added successfully!")

# Task 3: Update
sql_update = "UPDATE employee SET Salary = Salary * 1.1 WHERE Employee_Name = %s"
cursor.execute(sql_update, ("Rahul",))
connection.commit()
print("Salary updated successfully!")

cursor.close()
connection.close()