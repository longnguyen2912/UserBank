class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate= 0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0)]
    # other methods
    def showinfo(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        return self
    def make_deposit(self, amount, account_number=0):
        self.account[account_number].deposit(amount)
        return self
    def make_withdrawal(self, amount, account_number=0):
        self.account[account_number].withdraw(amount)
        return self
    def display_user_balance(self, account_number=0):
        self.account[account_number].display_account_info()
        return self
    def add_account(self):
        self.account.append(BankAccount(int_rate=0.02, balance=0))
        return self
    # your code here
user1 = User("John","johnkriss@gmail.com")
user1.showinfo().make_deposit(2000).make_withdrawal(500).display_user_balance()
user1.add_account().showinfo().make_deposit(1000,account_number=1).make_withdrawal(800,account_number=1).display_user_balance(account_number=1)
