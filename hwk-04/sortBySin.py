import math

list = eval(input())


def sortBySin(list):
    return sorted(list, key=math.sin)


print(sortBySin(list))
