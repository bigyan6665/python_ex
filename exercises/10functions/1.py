length = input("Enter length of rectangle = ")
breadth = input("Enter length of rectangle = ")


def area(l, b):
    print(f"Area of rectangle = {l*b}")


def perimeter(l, b):
    print(f"Perimeter of rectangle = {2*(l + b)}")


if length.isnumeric() and breadth.isnumeric():
    length = float(length)
    breadth = float(breadth)
    area(length, breadth)
    perimeter(length, breadth)
else:
    print("Enter valid data")
