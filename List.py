latter=['a',"b","c","d","e","f"]

print(len(latter))

latter.sort()
print(latter)



print(latter)
print(latter[0])
print(latter[3])
print(latter[2:])
print(latter[:3])
print(latter[:-2])
print(latter[-3:])

#data insert
print(latter+["g","h","i","25"])

latter.append("20") #one value we can append here
print(latter)
latter.insert(2,50)
print(latter)

print("a" in latter)
print("a" not in latter)

print("z" in latter)

latter.reverse()
print(latter)

latter.pop()
print(latter)

latter2=latter.copy()
print(latter2)

print(latter.count("d")) #shows how many same number here
print(latter.index("d"))















