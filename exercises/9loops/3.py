num = int(input("Enter the number whose factoral is to be found = "))

# using for loop
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"factorial of {num} = {factorial}")

# using while loop
i = 1
factorial = 1
while(i<=num):
    factorial = factorial * i 
    i = i+1
print(f"factorial of {num} = {factorial}")