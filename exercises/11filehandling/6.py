import json

students = {
    "9843": {"name": "Bigyan", "course": "Python", "age": 20},
    "9844": {"name": "Sandesh", "course": "Java", "age": 20},
    "9845": {"name": "Prajal", "course": "Python", "age": 20},
    "9846": {"name": "Dinesh", "course": "Java", "age": 20},
}
with open("info.json", "w") as file:
    json.dump(students, file)
