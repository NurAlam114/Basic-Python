class student():
#constructor ke call dite hoy na
    def __init__(self,roll,age):
        self.roll=roll
        self.age=age

    def display(self):
        print(f"roll:{self.roll},age:{self.age}")

rahim=student(101,20)
rahim.display()

karim=student(102,22)
karim.display()
