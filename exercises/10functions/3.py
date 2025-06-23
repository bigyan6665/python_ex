student = input("Enter name = ")
course = input("Enter course = ")

def show(name , course1 = "python"):
    print(f"Hello, {name}, Welcome to course {course1}")

if course == '':
    show(student)
else:
    show(student,course)
