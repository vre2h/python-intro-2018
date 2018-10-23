import sys

sys.setrecursionlimit(10000)
c1, c2, rad = eval(input())
isInCircle = True


def dots():
    d1, d2 = eval(input())
    global isInCircle

    if d1 == 0 and d2 == 0:
        return print('YES') if isInCircle else print('NO')
    elif ((d1 - c1) ** 2) + ((d2 - c2) ** 2) > rad ** 2:
        isInCircle = False

    return dots()


dots()
