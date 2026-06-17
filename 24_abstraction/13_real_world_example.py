from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment Successful")

upi = UPI()

upi.pay()