class Student():
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"roll: {self.roll}, gpa: {self.gpa}")

rahim = Student()
rahim.set_value(101,3.45)
print("rahim details")
rahim.display()

#print(f"r_roll: {rahim.roll}, r_gpa: {rahim.gpa}")



karim = Student()
karim.set_value(102,3.44)
print("karim details")
karim.display()

