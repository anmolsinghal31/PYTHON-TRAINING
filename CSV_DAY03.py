import csv
with open("student.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Robin","23","18"])