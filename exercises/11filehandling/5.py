with open("1python_essay.txt", "r") as file:
    data = file.read()  # data = string
    word_list = data.split(" ")  # word_list = list
    # print(word_list)
    trimed_word_list = [
        word.strip(" ,.\n    ")
        for word in word_list
        if word  # string returns False if it is empty otherwise True
    ]
    # print(trimed_word_list)
    # print(len(trimed_word_list))
    trimed_word_set = set(trimed_word_list)
    # print(trimed_word_set)
    # print(len(trimed_word_set))

    my_dict = {}
    for i in trimed_word_list:
        my_dict[i] = trimed_word_list.count(i)
    # print(my_dict.items())
    most_repeated = list(max(my_dict.items(), key=lambda item: item[1]))
    print(most_repeated)
