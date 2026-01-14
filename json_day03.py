import json

data={
    "name":"Anmol",
    "Age":23,
    "skills":["python"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=4)