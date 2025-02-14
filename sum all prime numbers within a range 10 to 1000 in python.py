prime_sum = 0

for num in range(10, 1000 + 1):
  #  if num > 1:

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
            prime_sum += num
print("prime number sumation is: ",prime_sum)