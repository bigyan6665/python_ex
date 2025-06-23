# a = 2
# print(a)
# # sciencese
# # virtual env
# linter(black)
# windsurf
# spell checker

# # iterator
# ls = [22, 44, 33]
# itr = iter(ls)

# # print(next(itr))
# # print(next(itr))
# # print(next(itr))

# # or

# for i in itr:
#     print(i)


# # generator
# # generators returns an iterator that contains series of values
# def custom_gen(x, y):
#     while x < y:
#         yield x
#         x = x + 1


# res = custom_gen(1, 100000000000000000)
# for i in res:
#     print(i)
#     if i > 2:
#         break

for i in range(
    1,
    1000000000000000000000000000,
):
    if i > 5:
        break
    print(i)


# # file handling

# # line by line reading
# file = open("new.txt", "r")
# for line in file:
#     print(line)
# file.close()
# # or
# file = open("new.txt", "r")
# print(file.readlines())
# file.close()

# # entire file reading
# file = open("new.txt", "r")
# print(file.read())
# file.close()

# # writting to file
# file = open("new.txt", "w")
# file.write("Hello Bigyan\n")
# file.write("Hello Dinesh")
# file.close()

# # context manager
# with open("new.txt", "w") as file:
#     file.write("Hello Bigyan\n")
#     file.write("Hello Bigyan")

# # same directory vanda bahira file handle garda absolute path dine ..yesari path leko xa
# import os

# file_path = os.path.join("E:\\python_exercise", "new.txt")
# print(file_path)

# with open(file_path, "w") as file:
#     file.write("using os\n")


# # appending to file
# with open(file_path, "a") as file:
#     file.write("appended\n")


# reading csv file
import csv

# reading as list
# with open("csvfile.csv", "r") as file:
#     reader = csv.reader(file) # list format ma data auxa
#     for row in reader:
#         print(row)

# reading as dictionary
# with open("csvfile.csv", "r") as file:
#     reader = csv.DictReader(file)  # dict format ma data auxa
#     for row in reader:
#         print(row)

# # writting list of list to csv file
# data = [["course", " student"], ["python", " 15"], ["java", " 35"]]
# with open("csvfile.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# # writting list of dictionary to csv file
# data = [{"course": "python", " student": " 15"}, {"course": "java", " student": " 12"}]
# with open("csvfile.csv", "w", newline="") as file:
#     header = ["course", " student"]
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(data)
