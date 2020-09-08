from math import sqrt


def findPrime(num: int):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return "NUM is not a prime"
        else:
            return "NUM is a prime"


print(findPrime(33))
print(findPrime(19))
print(findPrime(17))
print(findPrime(50))
print(findPrime(34))
