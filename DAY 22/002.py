from pymongo import MongoClient

# 1. Connect
client = MongoClient("mongodb://localhost:27017/")

# 2. Select Database and Collection
db = client["Company_DB"]
collection = db["C1"]

# 3. Create the data
new_employee = {"Name": "Reddy", "Salary": 10000}

# 4. Insert and FORCE it to finish
result = collection.insert_one(new_employee)

# 5. This print is important! If you see this, it worked.
print("Successfully inserted Reddy with ID:", result.inserted_id)