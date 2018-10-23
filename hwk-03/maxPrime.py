import math

a = int(input())


def maxPrime(a):
    i, j = a, 1

    while (i >= 2):
        while (j <= math.sqrt(i)):
            j += 1
            if i % j == 0:
                break
        else:
            return i
        i -= 1
        j = 1


print(maxPrime(a))
