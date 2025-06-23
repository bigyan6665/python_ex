import csv, json

with open("info.csv", "r") as csv_file, open("info_copy.json", "w") as json_file:
    reader = csv.DictReader(csv_file)
    new_dict = dict()
    for row in reader:
        # print(row)
        # print(row["contact"])
        contact = row["contact"]
        row.pop("contact")
        # print(row)
        new_dict[contact] = row

    # print(new_dict)
    json.dump(new_dict, json_file)
