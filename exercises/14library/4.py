import csv, random

csv_data_lod = list()
with open("exercises\\14library\\info.csv", "r") as file:
    reader = csv.DictReader(file)
    for x in reader:
        # print(x)
        csv_data_lod.append(x)

# print(csv_data_lod)
winners = random.sample(csv_data_lod, 3)
print(winners)


from mailerpy import Mailer

PASSWORD = "rzzx lygi gapz lbfr"
student_info = winners
try:
    my_mailer = Mailer("smtp.gmail.com", "587", "bigyans04@gmail.com", PASSWORD)
    for std in student_info:
        name = std["Name"]
        email = std["Email"]
        mail_content = f"Congratulation {name}, you won"
        my_mailer.send_mail([email], "From python", mail_content)
except Exception as e:
    print(f"Error = {e}")
