# Write a function can_drink that takes age as argument checks if user can drink.
# If user is 18+, return True else return False.
# Note: You need to raise TypeError if age is not integer value, ValueError if age is below 0, AssertionError if age is above 100.


def can_drink(age):
    if type(age) != int:
        raise TypeError("Do not enter non-integer value")
    else:
        assert age <= 100, "Age cannot be above 100"
        if age <= 0:
            raise ValueError("Age cannot be below 1")
        elif age >= 18:
            return True
        elif age < 18:
            return False


# If you import 'one' in another script, this block will still run. To prevent that, wrap it in:
if __name__ == "__main__":
    try:
        print(can_drink(3))
    except Exception as e:
        print(f"Error = {e}")
# This makes it behave like a module instead of a script when imported.
