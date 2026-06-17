# Abstract Class નું Object Create કરી શકાતું નથી.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

animal = Animal()