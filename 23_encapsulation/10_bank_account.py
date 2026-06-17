class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

account = BankAccount()

print(account.get_balance())