class phone:
    def __init__(self):
        print("this is phone class")


class samsung(phone):
    def __init__(self): #this is Overriding
        super().__init__() #when i am showing super class and sub class
        print("this is samsung class")

s = samsung()