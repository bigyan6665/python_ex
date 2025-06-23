class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    @property
    def balance(self):
        print(f"Owner = {self.owner}")
        print(f"Balance = {self.__balance}")

    def deposit(self, deposit_amt):
        if deposit_amt > 0:
            self.__balance += deposit_amt
        else:
            print("Deposit amount must be positive")

    def withdraw(self, withdraw_amt):
        if withdraw_amt > 0:
            if withdraw_amt <= self.__balance:
                self.__balance -= withdraw_amt
                print(f"Remaining balance = {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Withdraw amount must be positive")

    def transfer(self, to, transfer_amt):
        #
        if transfer_amt <= self.__balance:
            self.__balance -= transfer_amt
            to.__balance += transfer_amt
            print(f"Remaining balance = {self.__balance}")
        else:
            print("Insufficient balance")


ram = BankAccount("ram")
ram.deposit(1000)
ram.balance

hari = BankAccount("hari")
hari.deposit(1000)
hari.balance

print("\nAfter transfer")
ram.transfer(hari, 500)
ram.balance
hari.balance
