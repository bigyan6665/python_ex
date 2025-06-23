# os
# random
# math
# functools(reduce)
# mailerpy


# import os

# os.mkdir("pythonLab") # makes new directory inside current directory
# os.rename("pythonLab", "pythonLAB") # renames directory
# print(f"{os.path.getsize("E:\\python_exercise\\day2.py")} bytes") # returns size of directory in bytes
# os.remove("pythonLAB") # removes directory
# print(os.path.exists("pythonLAB")) # checks if a directory exists or not
# print(os.listdir("5list")) # returns the list of sub directories present inside a given dir


# import random

# ls = ["Hari", "Shyam", "Ram"]
# print(random.choice(ls))  # randomly selects an item from a list
# print(random.sample(ls, 2))  # randomly selects 2 items from a list

# print(random.random())  # randomly generates a value between 0-1
# print(random.randint(1, 10)) # randomly generates a integer between 1-10(both 1 and 10 inclusive)

# ls = ["Hari", "Shyam", "Ram"]
# random.shuffle(ls)
# print(ls)


# import math

# print(math.floor(3.5))
# print(math.ceil(3.5))
# print(math.pow(3, 3))
# print(math.pi)

# from functools import reduce

# ls = [4, 6, 8]
# product = reduce(lambda x, y: x * y, ls)
# print(product)


from mailerpy import Mailer

PASSWORD = "rzzx lygi gapz lbfr"
student_info = {"1": {"name": "Bigyan", "email": "bedhrajshrestha@gmail.com"}}
try:
    my_mailer = Mailer("smtp.gmail.com", "587", "bigyans04@gmail.com", PASSWORD)
    for roll_no, std in student_info.items():
        name = std["name"]
        email = std["email"]
        mail_content = f"Hello {name}, you are a good boy"
        my_mailer.send_mail([email], "From python", mail_content.format(name=name))
except Exception as e:
    print(f"Error = {e}")


# import requests

# url = ""
# data = requests.get(url)
