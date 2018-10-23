a = eval(input())


def SecondMax(a):
    min = a[0]

    for item in a:
        if item < min:
            min = item

    max, smax = min, min
    isSec = False

    for item in a:
        if item > max:
            smax = max
            max = item
            isSec = True
        elif max > item > smax:
            smax = item
            isSec = True

    return smax if isSec else 'NO'


print(SecondMax(a))
