import random

options = ["rock", "scissor", "paper"]
computer = random.choice(options)
user = input("Enter rock or, scissor or, paper = ").lower()
if (
    (computer == "rock" and user == "scissor")
    or (computer == "scissor" and user == "paper")
    or (computer == "paper" and user == "rock")
):
    print(f"computer = {computer}. You Loose")
elif (
    (user == "rock" and computer == "scissor")
    or (user == "scissor" and computer == "paper")
    or (user == "paper" and computer == "rock")
):
    print(f"computer = {computer}. You Win")
else:
    print(f"computer = {computer}. Draw")
