operations = ['*', '+', '-']


def clearExp(exp):
    exp = exp.split(' ')
    newExp = ()

    for i in exp:
        isInt = True

        try:
            int(i)
        except:
            isInt = False

        if isInt or i in operations:
            newExp = (*newExp, i)

    return newExp


def polCalc(list):

    if (len(list) < 3):
        return list[-1]

    for key, value in enumerate(list):
        if value in operations:
            val = eval(f'{list[key - 2]} {value} {list[key - 1]}')
            newList = (*list[0:key-2], val, *list[key + 1:])
            return polCalc(newList)


exp = input()
filtered = clearExp(exp)
print(polCalc(filtered))
