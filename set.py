num1 = {1,2,3,4,5,6}
num2 = set([5,6,7,8,9])

num2.add(19)
num2.remove(19)
print(num2)
num2.update(9,6)

print(10 in num2)
print(8 not in num1)

print("Union: ",num1 | num2)
print("Entersection: ",num1 & num2)
print("division: ",num1 - num2)
