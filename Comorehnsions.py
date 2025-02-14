#map function to comprehsions
num = [2,3,4,5,6]
print(list(map(lambda x: x*x,num)))

#comprehsions
num = [1,2,3,4,5,6,8]
print([x*x for x in num])

#filter function to comprehsions
num = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x: x%2==0,num)))

#comprehsions
num = [1,2,3,4,5,6,7,8]
print(x for x in num if x%2==0)