# 5. Create a Hangman with user option to choose level.
# There has to be level as Easy, Difficult and Hard.
# Words for this game taken from json file that has words separated on the basis of level.
# If user is able to guess word in 5 attempt display You Win else You Loose, Word was {word}.
# [Note: first & last letter has to be pre-filled and there should be short description as hint for each word in json]

import json, random


level = input("Enter level[easy,difficult,hard] = ").lower()
with open("exercises\\14library\\hangman.json") as file:
    data = json.load(file)
    word_hint = random.choice(data[level])
    word = word_hint[0]
    hint = word_hint[1]

attempt = 5
print(f"Level = {level}")
print(f"Hint = {hint}")
while attempt > 0:
    word_user = input("Guess the word = ")
    if word_user == word:
        print("You won")
        break
    else:
        attempt = attempt - 1
        if attempt == 0:
            print(f"You loose. Word was {word}")
        else:
            print(f"Try again. You have {attempt} attempts left")
