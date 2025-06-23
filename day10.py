# json
import json

# # python dict to json = serialization
# mydict = {"course": "python", " student": " 15"}
# json_string = json.dumps(mydict)
# print(json_string)

# # writting dict to json file
# mydict = {"course": "python", " student": " 15"}
# with open("json_file.json", "w") as file:
#     json.dump(mydict, file)

# deserialization
# json ma double quotes use hunxa
data = '{"course": "python", "student": "15"}'
dict_data = json.loads(data)
print(type(dict_data))
print(dict_data)

# # reading data from json file
# with open("json_file.json", "r") as file:
#     data = json.load(file)
#     print(data)
