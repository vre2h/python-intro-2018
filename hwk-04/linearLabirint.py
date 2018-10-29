list = eval(input())


def linearLabirint(list):
    dict = {}

    if len(set(list)) == 1:
        return 'NO'

    for i, j in enumerate(list):
        if (i >= 0 and i - 1 > 0):
            dict[i] = (list[i] + i, i - 1)
        elif (i >= 0):
            if (list[i] + i > len(list)):
                return 'NO'
            dict[i] = (list[i] + i,)

    for (i, j) in dict.items():
        for item in j:
            if (item == len(list) - 1):
                return 'YES'

    return 'NO'


print(linearLabirint(list))
