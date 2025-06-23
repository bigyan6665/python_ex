import datetime

dob = input("Enter DOB = ")
parsed_dob = datetime.datetime.strptime(dob, "%Y/%m/%d")
year = parsed_dob.strftime("%Y")
month_name_short = parsed_dob.strftime("%b")
month_num = int(parsed_dob.strftime("%m"))
day = parsed_dob.strftime("%d")
print(f"{year}{month_num*'*'}{month_name_short}{int(day[0]) * "*"}{day}")
