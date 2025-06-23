name = input("Enter name = ")
birth_year = int(input("Enter birth year = "))
present_year = 2025
age = present_year - birth_year
if(age >=18 and age<=70):
    print(f"{name}, you are eligible for voting")
else:
    print(f"{name}, you arenot eligible for voting")