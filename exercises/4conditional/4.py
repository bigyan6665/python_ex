'''
4.take 2 numbers form user and print the largest
'''
num1 = float(input("Enter num1 = "))
num2 = float(input("Enter num2 = "))
if(num1 > num2):
    print(f"{num1} is largest")
elif(num2 > num1):
    print(f"{num2} is largest")
else:
    print("Both are equal")