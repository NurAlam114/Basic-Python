from collections import deque

bank = deque(["nabil","nur","alam"])

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)
if not bank:
    print("no person left")

