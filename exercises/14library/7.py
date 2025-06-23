import os

path = "E:\\python_exercise\\exercises"
all_topics = os.listdir(path)  # list type
# print(all_topics)
dict_a = dict()  # {topic:no_of_exercise}
for topic in all_topics:
    topic_path = os.path.join(path, topic)
    # print(topic_path)
    exercise_count = len(os.listdir(topic_path))  # do not count csv files
    dict_a[topic] = exercise_count


for topic in dict_a.items():
    print(topic)
