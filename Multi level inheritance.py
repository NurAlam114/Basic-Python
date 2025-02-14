class A:
    def display(self):
        print("this is A class.")

class B(A):
    def display1(self):
        print("this is B class. which is inclde A class.")

class C(B):
    def display2(self):
        super().display()
        super().display1()
        print("this is C class, which is include A and B class.")

obj = C()
obj.display2()