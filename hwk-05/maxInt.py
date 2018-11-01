def maxInt(str):
    return max([int(s) for s in str.split() if s.replace('-', '', 1).isdigit()])


a = input()
str = []
while a != '':
    str.append(a)
    a = input()

text = '\n'.join(str)

print(maxInt(text))
