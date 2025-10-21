import json
pythonObject = {
    "Ten":"Tran Duy Thanh",
    "Tuoi":50,
    "Ma":"nv1"
}

jsonString = json.dumps(pythonObject)
print(jsonString)