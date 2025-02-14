#Named function
def calculate(a,b):
    return a*a + 2*a*b + b*b
print(calculate(10,20))

#Lambda function

print((lambda a,b : a*a + 2*a*b + b*b)(10,20))

print((lambda a,b : a+b)(10,10))