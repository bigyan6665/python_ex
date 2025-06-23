'''
3.get marks as input from user and display grade.
(>=90 - A,>=80 - B,>=70 - C,>=60 - D,<60 - F)
'''
marks = float(input("Enter marks = "))
if(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
elif(marks >= 60):
    print("D")
elif(marks < 60):
    print("F")