from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass

class P(Clothes):
    def __init__(self, V):
        self.V = V

    def calc(self):
        return self.V/6.5 + 0.5

    @property
    def getV(self):
        return self.V

class H(Clothes):
    def __init__(self, H):
        self.H = H

    def calc(self):
        return self.H*2 + 0.3

p1 = P(2)
print(p1.calc())
print(p1.getV)
h1 = H(3)
print(h1.calc())