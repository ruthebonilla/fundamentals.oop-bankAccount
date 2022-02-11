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
        print("Balance:" + str(self.balance))
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance* self.int_rate
        return self
    



# account1 = BankAccount()
# account2 = BankAccount()

# account1.deposit(30).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
# account2.deposit(50).deposit(50).withdraw(30).withdraw(20).withdraw(30).withdraw(30).yield_interest().display_account_info()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class User:
    
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.01, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        print("User:" + str(self.name), "Balance: "+ str(self.account.balance))
        return self

    # def transfer_money(self, amount, animal):
    #         self.amount -= amount
    #         animal.amount += amount
    #         self.display_user_balance()
    #         animal.display_user_balance()
    #         return self

user1 = User("Panda")
user2 = User("Turtle")
user3 = User("Parrot")

user1.make_deposit(400).make_deposit(100).make_deposit(800).make_withdrawl(200).display_user_balance()
user2.make_deposit(200).make_deposit(200).make_withdrawl(50).make_withdrawl(50).display_user_balance()
user3.make_deposit(700).make_withdrawl(100).make_withdrawl(300).make_withdrawl(300).display_user_balance()

# print("*Panda transfers money to his friend Parrot*")
# user1.transfer_money(300, user3)