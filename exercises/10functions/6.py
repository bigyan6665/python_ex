string = "pineapple"
st = set(string)
print(st)
dict = {}

for i in st:
    dict[i] = string.count(i)

print(dict)