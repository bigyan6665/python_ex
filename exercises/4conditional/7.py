name = input("Enter name = ")
age = int(input("Enter age = "))
salary = float(input("Enter salary = "))
if(age >=21 and salary>=25000):
    print(f"{name}, you are eligible for loan")
else:
    print(f"{name}, you arenot eligible for loan")