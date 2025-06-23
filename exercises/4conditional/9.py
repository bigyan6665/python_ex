balance = 100000
withdraw = float(input("Enter amount to withdraw = "))
if(withdraw <= balance):
    remaining = balance - withdraw
    print(f"{withdraw} withdrawn successfully")
    print(f"New balance : {remaining} ")
else:
    print("Insufficient balance")

