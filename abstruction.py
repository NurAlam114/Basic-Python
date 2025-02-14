from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self,base, height):
        self.base = base
        self. height = height

    @abstractmethod
    def area(self):
        pass
class traiangle(shape):
    def area(self):
        area =  0.5 * self.base * self.height
        print("traiangle",area)

class ractangle(shape):
    def area(self):
        area = self.base * self.height
        print("ractangle",area)

        #ekhane area polymorphism hisabe ache karon .ekhane area method bivinno somoye bivinno calculate korche

t1 = traiangle(10,10)
t1.area()
r1 = ractangle(10,10)
r1.area()


