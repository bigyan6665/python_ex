# exception handling

# exception
# syntax:
# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

# 1.built in exception: ZeroDivisionError, TypeError, ValueError, AssertionError
# user_input = input("Enter 2 comma separate values = ").split(",")
# try:
#     num1, num2 = map(
#         lambda num: float(num.strip()), user_input
#     )  # code below errored line is not executed
#     print(num1 / num2)
# except ZeroDivisionError as e:
#     print(f"Error = {e}")
#     print("you cannot divide by zero")
# except Exception as e:
#     print(f"Error = {e}")
# except:
#     print("you provided incorrect numbers")
# else:
#     print(num1 / num2)
# finally:
#     print("Thanks for using this program")


# 2.user-defined exception/raising error
def license_eligibility(age):
    if age < 0:
        raise ValueError("Age must be greater than 0")
    if type(age) != int:
        raise TypeError("Age must be integer")
    if age < 18:
        raise Exception("Your age is less than 18")


try:
    license_eligibility(45)
except Exception as e:
    print(f"Error = {e}")
else:
    print("Eligible for license")


# # Assertion = raise with condition
# # Syntax: assert_condition,[error msg]
# def area_calc(l, b):
#     assert l > 0, "Length cannot be less than 1"
#     assert b > 0, "breadth cannot be less than 1"
#     return l * b


# print(area_calc(-1, 3))
