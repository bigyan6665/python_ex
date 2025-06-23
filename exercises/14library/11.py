import datetime

dob = input("Enter DOB = ")
parsed_dob = datetime.datetime.strptime(dob, "%Y/%m/%d")
current = datetime.datetime.now()
days_passed = current - parsed_dob
print(f"{days_passed.days} days passed since birth")
