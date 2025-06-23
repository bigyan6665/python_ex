# # unpacking
# # 1.tuple unpacking
# tp = ("python",2,"broadway")
# course_name , duration,institute = tp
# print(course_name)
# print(duration)
# print(institute)

# # course_name , duration = tp # error
# # print(course_name)
# # print(duration)








# dictionary = mutable data type , key value pairs
# keys must be unique , immutable

# # method1
# dt = {"name":"Bigyan","rol_no":23}
# # method2
# keys = ['name',"roll_no"]
# values = ["bigyan",23]
# zp = zip(keys,values)
# print(zp)
# dt = dict(zp)
# print(dt)

# dt = {"name":"Bigyan","rol_no":23}
# print(dt['name']) # throws error if not found
# print(dt.get("salary","not found")) # throws none or given text if not found
# # changes done
# dt['name'] = "hari"
# print(dt)
# # adds new pair
# dt['salary'] = 25000
# print(dt)

# students = {
#     "student1": {
#         "name": "Alice",
#         "age": 20,
#         "grades": {
#             "math": 85,
#             "science": 92
#         }
#     },
#     "student2": {
#         "name": "Bob",
#         "age": 22,
#         "grades": {
#             "math": 78,
#             "science": 88
#         }
#     }
# }

# # Accessing data
# print(students["student1"]["name"])        # Output: Alice
# print(students["student2"]["grades"]["math"])  # Output: 78


# # getting keys,values and clear
# dt = {"name":"Bigyan","roll_no":23}
# print(dt.keys())
# print(dt.values())
# print(dt.items())
# dt.clear()
# print(dt)

# # pop
# dt = {"name":"Bigyan","roll_no":23}
# print(dt.pop("name"))
# print(dt)

# # len
# dt = {"name":"Bigyan","roll_no":23}
# print(len(dt))

# # copy
# dt1 = {"name":"Bigyan","roll_no":23}
# dt2  = dt1.copy()
# print(dt2)

# # update = merge 2 dicts and same keyed values rae updated
# dt1 = {"name":"Bigyan","roll_no":23}
# dt2 = {"name":"hari","salary":5000}
# dt1.update(dt2)
# print(dt1)

# # containnment
# dt1 = {"name":"Bigyan","roll_no":23}
# print("name" in dt1) # search in keys





# # range
# print(list(range(5,10,2))) # start , end , jump




# loop
# 1.for loop
# 2.while loop

# string = "Bigyan"
# for x in string:
#     print(x)

# ls = [22,33,44,55]
# for x in ls:
#     print(x)

dt1 = {"name":"Bigyan","roll_no":23}
for k,v in dt1.items():
    print(f"{k} = {v}")
