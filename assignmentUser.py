class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount
        
    def make_withdrawl(self, amount):
        self.amount -= amount
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        
    def transfer_money(self, amount, animal):
            self.amount -= amount
            animal.amount += amount
            self.display_user_balance()
            animal.display_user_balance()
        
user1 = User("Panda")
user2 = User("Turtle")
user3 = User("Parrot")

user1.make_deposit(400)
user1.make_deposit(100)
user1.make_deposit(800)
user1.make_withdrawl(200)
user1.display_user_balance()

user2.make_deposit(200)
user2.make_deposit(200)
user2.make_withdrawl(50)
user2.make_withdrawl(50)
user2.display_user_balance()

user3.make_deposit(700)
user3.make_withdrawl(100)
user3.make_withdrawl(300)
user3.make_withdrawl(300)
user3.display_user_balance()

print("*Panda transfers money to his friend Parrot*")
user1.transfer_money(300, user3)