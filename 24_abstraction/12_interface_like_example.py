from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_data(self):
        pass


class Report(Printable):

    def print_data(self):
        print("Printing Report")

report = Report()

report.print_data()