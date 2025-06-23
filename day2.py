# .format
# fstring
# user input
# comment
# operators

fruit = "apple"
price = 300.3333
print(f"{fruit:+>15} = {price:07.2f}") # > by default when number < by default when string
print("{fruit} = {price}".format(fruit = fruit,price = price))