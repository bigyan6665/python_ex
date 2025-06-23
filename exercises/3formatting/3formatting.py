# '''
# 1.get customer's name and pen price as user input and print using the format:
# Ram bought a pen for Rs.50.00(Note 2 decimal points) 
# '''
# customer_name = input("Enter customer's name = ")
# pen_price = float(input("Enter pen price = "))
# print(f"{customer_name.title()} bought a pen for Rs.{pen_price:.2f}")


# '''
# 2.get 3 fruit name and its price and print the format:(align fruit name left with 12 spaces)

# Item        Price
# -------------------
# Apple       Rs. 30
# Mango       Rs. 50

# '''
# fruit1 = input("Enter fruit name1 = ")
# price1 = float(input("Enter price1 = "))
# fruit2 = input("Enter fruit name2 = ")
# price2 = float(input("Enter price2 = "))
# fruit3 = input("Enter fruit name3 = ")
# price3 = float(input("Enter price3 = "))
# print(f"{"Item":<12}Price")
# print(f"{"":-<20}")
# print(f"{fruit1:<12}Rs. {price1}")
# print(f"{fruit2:<12}Rs. {price2}")
# print(f"{fruit3:<12}Rs. {price3}")


# '''
# 3.take input of name and marks.Display marks percentage if total is 80.
# output format:Ram, you have scores 85.67% in exam
# '''
# name = input("Enter name = ")
# marks = float(input("Enter  marks = "))
# percentage = marks/80 * 100
# print(f"{name.title()}, you have scored {percentage:.2f}% in exam")


'''
4.Take input of year,month and day and print full date in the format:yyyy/mm/dd
'''
year = int(input("Enter year = "))
month = int(input("Enter month = "))
day = int(input("Enter day = "))
print(f"{year}/{month:02}/{day:02}") 