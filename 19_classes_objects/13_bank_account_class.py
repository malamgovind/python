class Bankaccount:

    def __init__(self, amount):
        self.amount = amount

account = Bankaccount(1000000)
print(account.amount)