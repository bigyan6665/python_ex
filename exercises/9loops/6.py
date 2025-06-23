dt = {'9843': {'course': 'python', 'name': 'abc', 'present': True}, '984': {'course': 'c', 'name': 'efg', 'present': False}}
print(dt.values())
for inner_dict in dt.values():
    if inner_dict.get("present") == False and inner_dict.get("course") == 'python':
        print(inner_dict.get("name"))

