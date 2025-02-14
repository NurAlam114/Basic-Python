from random import randint

for x in range(1,4):
    geussNumber = int(input("Enter your geuss number(1-5): "))
    randomNumber = randint(1, 5)

    if geussNumber == randomNumber:
        print("You won")

    else:
        print("You loss")
        print("Random number was: ", geussNumber)


