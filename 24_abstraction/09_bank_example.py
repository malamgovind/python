from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass


class SBI(Bank):

    def interest(self):
        print("7% Interest")

sbi = SBI()

sbi.interest()