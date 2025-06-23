# Your company is hosting a party. Detail of employee is stored in info.csv containing name,DOB,mobile_number.
#  Write a program that reads csv file, determines number of soft drink or hard drink required and store result in JSON file as:
# {“hard_drink”: num_1, “soft_drink”: num_2}.
# Assume 1 drink per user and use function of 1 and 2 to determine the drink for user

import csv, one, two, json

result = {"hard_drink": 0, "soft_drink": 0}

with open(
    "E:\\python_exercise\\exercises\\12exception_handling\\info.csv", "r"
) as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row["DOB"])
        dob = row["DOB"]
        try:
            age = two.age_calculator(dob)
            eligible = one.can_drink(age)
        except Exception as e:
            print(f"Error with {row['Name']} = {e}")
        else:
            if eligible:
                print(f"{row['Name']} is eligible")
                result["hard_drink"] += 1
            else:
                print(f"{row['Name']} isnot eligible")
                result["soft_drink"] += 1

print(result)


with open(
    "E:\\python_exercise\\exercises\\12exception_handling\\drinks.json", "w"
) as file:
    json.dump(result, file)
