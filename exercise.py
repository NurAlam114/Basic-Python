class Triangle():

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def display(self):
        print(0.5*self.base *self.height)

formula= Triangle(10,20)
formula.display()
formula= Triangle(20,30)
formula.display()

