from functools import reduce

ls = [2, 4, 6]
product = reduce(lambda x, y: x * y, ls)
print(product)
