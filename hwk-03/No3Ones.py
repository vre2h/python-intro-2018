n = int(input())


def No3Ones(n):
    list = 2, 4, 7

    if n == 1:
        return list[0]
    elif n == 2:
        return list[1]
    elif n == 3:
        return list[2]
    elif n == 4:
        return list[0] + list[1] + list[2]

    i = 3

    while i < n:
        list += tuple((list[i - 1] + list[i - 2] + list[i - 3],))
        i += 1

    return list[n - 1]


print(No3Ones(n))
