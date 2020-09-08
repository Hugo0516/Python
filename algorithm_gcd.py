def findGcd(num1: int, num2: int):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


def findLcm(num1: int, num2: int):
    return num1 * num2 / findGcd(num1, num2)


print(findGcd(10, 8))

print(findGcd(20, 6))

print(findGcd(100, 66))

print(findGcd(121, 33))

print(findLcm(10, 8))

print(findLcm(20, 6))