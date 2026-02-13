from pymongo import MongoClient

try:
    # 1. Connect using the IP address
    client = MongoClient("mongodb://127.0.0.1:27017/", serverSelectionTimeoutMS=5000)

    # Using the name that already exists to avoid the "Case" error
    db = client["Company_DB"]
    collection = db["employees"]

    # TASK 1: Insert a new employee document
    new_emp = {"name": "Sanya", "department": "IT", "salary": 55000}
    collection.insert_one(new_emp)
    print("Task 1: Sanya inserted successfully into Company_DB!")

    # TASK 2: Find all employees in the "IT" department
    print("\nTask 2: IT Department Employees:")
    for emp in collection.find({"department": "IT"}):
        print(emp)

    # TASK 3: Update the salary of an employee with a given name
    collection.update_one({"name": "Sanya"}, {"$set": {"salary": 62000}})
    print("\nTask 3: Salary updated for Sanya!")

except Exception as e:
    print(f"Error: {e}")