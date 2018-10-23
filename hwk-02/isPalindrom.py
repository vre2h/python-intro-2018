n = eval(input())


def reverse(n, acc=0):
    if (n == 0):
        return acc
    else:
        return reverse((n // 10), acc * 10 + n % 10)


def isPalindrom(n):
    if n == 0:
        return print('YES')
    elif n % 10 == 0:
        return print('NO')
    reverted = reverse(n)
    return print('YES') if reverted == n else print('NO')


isPalindrom(n)
