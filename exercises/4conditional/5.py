'''
5.take 3 sides of a triangle and dsiplay if it is equilaterla,scalene or isoceles
'''
side1 = float(input("Enter side1 = "))
side2 = float(input("Enter side2 = "))
side3 = float(input("Enter side3 = "))
if(side1 == side2 == side3):
    print("Equilateral")
elif(side1 == side2 or side2 == side3 or side1 == side3 ):
    print("Isoceles")
else:
    print("scalene")