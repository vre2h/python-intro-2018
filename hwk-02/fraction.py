a, b = eval(input())


def fun(a, b, i=2):
    if a % b == 0:
        return print(a // b)
    elif b % a == 0:
        return print('{}/{}'.format(1, b // a))
    elif a // b == 0:
        return print('{}/{}'.format(a % b, b))
    elif (i == 10):
        return print("{} {}/{}".format(a // b, a % b, b))
    elif a % i == 0 and b % i == 0:
        return fun(a // i, b // i, 2)
    elif a % i != 0 or b % i != 0:
        return fun(a, b, i + 1)


fun(a, b)
