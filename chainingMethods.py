class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self, amount, animal):
            self.amount -= amount
            animal.amount += amount
            self.display_user_balance()
            animal.display_user_balance()
            return self



user1 = User("Panda")
user2 = User("Turtle")
user3 = User("Parrot")

user1.make_deposit(400).make_deposit(100).make_deposit(800).make_withdrawl(200).display_user_balance()
user2.make_deposit(200).make_deposit(200).make_withdrawl(50).make_withdrawl(50).display_user_balance()
user3.make_deposit(700).make_withdrawl(100).make_withdrawl(300).make_withdrawl(300).display_user_balance()

print("*Panda transfers money to his friend Parrot*")
user1.transfer_money(300, user3)