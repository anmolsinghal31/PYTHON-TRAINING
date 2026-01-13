student = {

    "name": "Anmol",
    "age": 22,
    "Course": "Python"

}
print(student)
print(student["name"])
print(student.get("age"))

student["Marks"] = 85
student["age"] = 25
print(student)
print(student["name"])
print(student.get("age"))
student.popitem()
print(student)

print(student.keys())
print(student.values())

for key in student:
    print(key, student[key])

if "name" in student:
    print("key exists")

employees={

    101:{"name":"Kiran","salary":4554},
    102:{"name":"Kiran","salary":4554},
}

print(employees[101]["name"])