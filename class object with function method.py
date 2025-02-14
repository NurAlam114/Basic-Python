class Student():
    roll = ""
    gpa = ""

    def display(self):
        print(f"roll : {self.roll} , gpa : {self.gpa}")

rahim = Student()
rahim.roll = 102
rahim.gpa = 3.45
rahim.display()

karim = Student()
karim.roll = 202
karim.gpa = 3.54
karim.display()
