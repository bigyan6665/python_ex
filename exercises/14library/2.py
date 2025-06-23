import random

correct = random.randint(1, 10)
attempt = 3
print("**********You've got 3 attempts**********")
while attempt > 0:
    attempt = attempt - 1
    num = int(input("Guess number from 1 - 10 = "))
    if num == correct:
        print("You Win!!!")
        break
    else:
        if num < correct:
            print("Incorrect!!! Correct number is greater than you guessed")
        else:
            print("Incorrect!!! Correct number is smaller than you guessed")
else:
    print(f"You Loose!!!\nCorrect number was {correct}")
