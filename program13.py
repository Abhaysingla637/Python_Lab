class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount

            if new_balance < 0:
                self.deposit(0 - new_balance)
                self.withdraw(0 - new_balance)
                return

            super().withdraw(amount)
        else:
            print("Overdraft limit exceeded")

    def display(self):
        super().display()
        print("Overdraft Limit:", self.overdraft_limit)


savings = SavingsAccount("Rahul", 10000, 4)
current = CurrentAccount("Aman", 5000, 2000)

print("\n--- Savings Account ---")
savings.display()
savings.deposit(2000)
savings.withdraw(1000)
print("Final Balance:", savings.get_balance())

print("\n--- Current Account ---")
current.display()
current.withdraw(6000)
print("Final Balance:", current.get_balance())

print("\n--- Polymorphism ---")
for account in [savings, current]:
    account.display()
