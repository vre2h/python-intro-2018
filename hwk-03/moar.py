def moar(a, b, n):
    counterA, counterB = 0, 0

    for item in a:
        if item % n == 0:
            counterA += 1

    for item in b:
        if item % n == 0:
            counterB += 1

    return True if counterA > counterB else False
