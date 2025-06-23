items = ['book','book','pen','pen','pen','pencil','marker']
# 1
print(items)
items.append("pen")
print(items)
# 2
print(f"No. of pencils = {items.count("pencil")}")
# 3
items.insert(2,"sticky_notes")
print(items)
# 4
items.remove('pencil')
print(items)
# 5
print(items.pop(1))
print(items)
# 6
print(items.pop(0))
print(items.pop(0))
print(items)
# 7
print(f"Total items = {len(items)}")
# 8
all = ",".join(items)
print(all)
# 9
print(items[1:3])
# 10
print(f"Pen lies in index = {items.index("pen")}")
print(f"Item on 3rd position = {items[3]}")