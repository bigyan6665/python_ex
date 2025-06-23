# 13. Scrape data from sharesansar and store in CSV. Name of CSV has to be the date on which scaping was done.Example: 2025_06_03_sharedata.csv.
# Also send this data to two of your application users. Keep yourself in cc & me in bcc: rabindrasapkota2@gmail.com

import requests, os, csv
from bs4 import BeautifulSoup
from datetime import datetime


def data_from_html(table_html):
    rows = table_html.find_all("tr")
    table_data = list()
    for row in rows:
        columns = row.find_all(["td", "th"])
        data = [column.get_text(strip=True) for column in columns]
        table_data.append(data)
    return table_data


url = "https://www.sharesansar.com/live-trading"
table_id = "headFixed"

response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Error with status code = {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
table_html = soup.find("table", {"id": table_id})
# print(table_html.prettify())
table_data = data_from_html(table_html)
for row in table_data:
    print(row)

today_full_date = datetime.now().strftime("%Y_%m_%d")
file_name = f"{today_full_date}_sharedata.csv"
file_path = os.path.join("exercises\\14library", file_name)

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(table_data)

from mailerpy import Mailer

PASSWORD = "rzzx lygi gapz lbfr"
student_info = {
    "1": {"name": "Bigyan", "email": "bedhrajshrestha@gmail.com"},
    "2": {"name": "Dinesh", "email": "bajagaindinesh21@gmail.com"},
}
try:
    bcc_email = "rabindrasapkota2@gmail.com"
    my_mailer = Mailer("smtp.gmail.com", "587", "bigyans04@gmail.com", PASSWORD)
    for roll_no, std in student_info.items():
        name = std["name"]
        email = std["email"]
        mail_content = f"Hello {name}, you are a good boy"
        my_mailer.send_mail(
            [email],
            "From python",
            mail_content.format(name=name),
            mail_cc=[email],
            mail_bcc=[bcc_email],
            attachments=[
                "E:\\python_exercise\\exercises\\14library\\2025_06_18_sharedata.csv"
            ],
        )
except Exception as e:
    print(f"Error = {e}")
