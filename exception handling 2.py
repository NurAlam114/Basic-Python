def voter(age):
    if age > 18:
        raise ValueError("Invalid voter")
    return "you can vote"

try:
    print(voter(17))
    print(voter(19))
except ValueError as e:
    print(e)