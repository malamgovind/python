class Account:

    def interest(self):
        print("General Interest")

class Savingaccount(Account):

    def interest(self):
        print("5% Intereser")

class Currentaccount(Account):

    def interest(self):
        print("2% Interest")

class Privateaccount(Account):
    pass

bank = [Savingaccount(), Currentaccount(), Privateaccount()]

for  accounts in bank:
    accounts.interest()