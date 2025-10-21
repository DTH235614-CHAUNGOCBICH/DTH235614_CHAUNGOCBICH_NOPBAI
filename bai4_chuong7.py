import json
jsonString = '{"ma":"nv1","age":"50","ten":"Trần Duy Thanh"}'
dataObject = json.loads(jsonString)
print(dataObject)
print("Mã nhân viên: ", dataObject["ma"])
print("Tuổi: ", dataObject["age"])
print("Tên nhân viên: ", dataObject["ten"])