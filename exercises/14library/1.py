import random

correct = random.randint(1, 10)
num = int(input("Guess number from 1 - 10 = "))
if num == correct:
    print("You Win!!!")
else:
    print(f"You Loose!!!\nCorrect number was {correct}")
