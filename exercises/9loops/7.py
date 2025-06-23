fruits = ['apple','Avocado','Pineapple','mango','watermelon']
new_fruits = [fruit.upper() if fruit.startswith("a") or fruit.startswith("A") else fruit.lower() for fruit in fruits]
print(new_fruits)