class shape:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        print("showing")

class triangle(shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print("Triangle: ", area)

class ractangle(shape):
    def area(self):
        area = self.base * self.height
        print("ractangle: ", area)

        #ekhane area polymorphism hisabe ache karon .ekhane area method bivinno somoye bivinno calculate korche

t1 = triangle(20,30)
t1.area()
t2 = ractangle(10,10)
t2.area()