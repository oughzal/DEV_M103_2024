from abc import ABC,abstractmethod
class Animal(ABC):

    @abstractmethod
    def sePlacer(self):
        pass

class Chat(Animal):
    pass

c1 = Chat()