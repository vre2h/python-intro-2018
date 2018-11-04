str1 = input()
str2 = input()


def shuffle(str1, str2):
    str1 = sorted(str1.upper().replace(',', ' ,').replace('!', ' !').replace(
        '.', ' .').replace('?', ' ?').replace(':', ' :').replace(';', ' ;').split(' '))
    str2 = sorted(str2.upper().replace(',', ' ,').replace('!', ' !').replace(
        '.', ' .').replace('?', ' ?').replace(':', ' :').replace(';', ' ;').split(' '))

    return ' '.join(str1) == ' '.join(str2)


print(shuffle(str1, str2))
