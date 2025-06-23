with open("3java.txt", "w") as java_file, open("1python_essay.txt", "r") as python_file:
    python_data = python_file.read()
    java_data = python_data.replace("Python", "Java")
    # print(python_data)
    # print(java_data)
    java_file.write(java_data)
