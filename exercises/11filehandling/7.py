import json, csv

with open("info.json", "r") as json_file, open("info.csv", "w", newline="") as csv_file:
    data = json.load(json_file)  # data = dictionary
    # print(data)
    for k, v in data.items():
        v["contact"] = k
    new_list = list(data.values())
    # print(new_list)

    header = list(new_list[0].keys())
    print(header)
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_list)
