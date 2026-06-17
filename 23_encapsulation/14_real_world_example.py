class ATM:

    def __init__(self):
        self.__pin = 12345

    def check_pin(self, pin):
        if pin == self.__pin:
            print("accese granted")
        else:
            print("pin wrong")


atm = ATM()
atm.check_pin(12355)
atm.check_pin(12345)