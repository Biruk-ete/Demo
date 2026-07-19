class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
    
    # TODO: withdraw(amount) — reject overdrafts
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    # TODO: statement() — print owner, number, balance
    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")


account1 = Account("Ephrem", 12749874, 4000)
account2 = Account("Meaza", 10008484, 2500)

print(account1.balance)

account1.deposit(2000)
account1.withdraw(2500)

print(account1.balance)

account1.statement()