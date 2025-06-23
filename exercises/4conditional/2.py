'''
2.get 2 input from user and display if first number is divisible by the second(21 is(not) divisible by 7)
'''
num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))
if(num1 % num2 == 0):
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} isnot divisible by {num2}")