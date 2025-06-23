
# '''
# 1.human normal body temperature is 98.6 degree f. what will this value be on degree celsius f = 1.8c + 32
# '''

# temp = input("Enter temperature in fahrenheit = ")
# temp_f = float(temp)
# temp_c = (temp_f-32)/1.8
# print(f"In fahrenheit , temperature = {temp_f:.2f}F In celsius, it is equals to {temp_c:.4f}C")


# '''
# 2.a firm deposited amount 50000 with interest rate 7.5%pa for 3 months.calculate the amount 
# '''
# principal = float(input("Enter principal = "))
# rate = float(input("Enter rate = "))
# time = float(input("Enter time(in months) = "))
# time_in_yrs = time / 12
# amount = principal + principal*time_in_yrs*rate/100 
# print(f"The amount = {amount}")


# '''
# 3.calculate area and perimeter of circle based on diameter
# '''
# diameter = input("Enter diameter = ")
# radius = float(diameter) / 2
# area = 3.14 * radius**2
# perimeter = 2 * 2.14 * radius
# print(f"Perimeter = {perimeter:.2f} \nArea =  {area:.2f}")


'''
5.display binary,octal and hex value of a given number
'''
num = int(input("enter num = "))
print(f"In binary, {num}={bin(num)}")
print(f"In octal, {num}={oct(num)}")
print(f"In hexadecimal, {num}={hex(num)}")