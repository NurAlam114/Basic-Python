import re
pattern = r"color"
if re.match(pattern,"color is a red, red is a color"):
    print("match")
else:
    print("not match")

if re.search(pattern,"color is red, red is good color"):
    print("found it")
else:
    print("no found")
###########              it is case sensitive

pattern = r"red"
print(re.findall(pattern,"red is a color ,red is very good color"))

print("another regular expression practice")

pattern = r"color"
text = "my favorite color is red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())


pattern = r"colour"
text = "red is colour, it is very good colour"
exg = re.sub(pattern,"color",text)
#exg = re.sub(pattern,"color",text,count=1) if we use count then it is first one exg in this text line
print(exg)

pattern = r"[a-d]"
if re.match(pattern, "xyz"):
    print("match")
else:
    print("not match")