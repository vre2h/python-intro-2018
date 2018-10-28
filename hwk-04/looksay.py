def finder(num):
    count = 1
    res = ''
    for i, j in enumerate(num):
        if (i + 1 < len(num) and num[i + 1] == j):
            count += 1
            continue
        res += '{}{}'.format(count, j)
        count = 1

    return res


num = '1'


def LookSay():
    global num
    while(True):
        for i in num:
            yield int(i)
        num = finder(num)
