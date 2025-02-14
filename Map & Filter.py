#map function
def square (x):
    return(x*x)

num = [2,4,6,8,10]

print(list(map(square,num)))


#Filter function

num = [1,2,3,4,5,6,7,8,9,10]

print(list((filter(lambda x : x%2==0 , num))))
