class A:
    def display(self):
        print("this is A class.")

class B:
    def display(self):
        print("this is B class.")

class C(A,B):
    def display(self):
        #we can use super() and print A and B class display print.
        print("this is C class, which include A and B class.")

#if we use this statement then here we will take that which class first, that class display will print.
# class C(A,B):
#     pass


obj = C()
obj.display()