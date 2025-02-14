def student(*details):   #details are all paramiters are allows
    print(details)  #print(details[0])

student(101,"nabil","hozoborolo")




def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
add(10,20)
add(20,10,30)
add(10,20,30,40)


# xx argument

def student (**details):
    print(details)    #print(details["age])

student(id=101,name="nabil",age=22)























