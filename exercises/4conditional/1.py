'''
1.get customer name and birth year from user input and display if he/she can vote:
Ram, You are(not) eligible for voting.(people with age 18 0r more can vote)
'''

name = input("Enter name = ")
birth_year = int(input("Enter your birth year = "))
present_year = 2025
age = present_year - birth_year
if(age >=18):
    print(f"{name}, You are eligible for voting")
else:
    print(f"{name}, You arenot eligible for voting")