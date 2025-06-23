# Create a function that calculates the age of user on passing DOB. [Hint: You can get current date from datetime library,
#  use AI tool for detail].
# Note: You need to raise Exception if DOB is in invalid format, if DOB is in future. Return value of age has to be integer number

import datetime
import time


def age_calculator(dob):
    date_obj = time.strptime(dob, "%d/%M/%Y")  # raise error if the format is mismatched
    birth_year = date_obj.tm_year
    current_year = int(datetime.datetime.now().strftime("%Y"))
    if birth_year > current_year:
        raise ValueError("Nobody can born in future")
    age = current_year - birth_year
    return age


# If you import 'two' in another script, the input() line will still run. To prevent that, wrap it in:
if __name__ == "__main__":
    dob = input("Enter date of birth [dd/mm/yyyy] = ")
    try:
        print(f"Age = {age_calculator(dob)} years")
    except Exception as e:
        print(f"Error = {e}")
# This makes it behave like a module instead of a script when imported.
