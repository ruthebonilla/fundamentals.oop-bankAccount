class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance* self.int_rate
        return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(30).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
account2.deposit(50).deposit(50).withdraw(30).withdraw(20).withdraw(30).withdraw(30).yield_interest().display_account_info()
