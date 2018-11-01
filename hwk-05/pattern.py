import re

text = input()
pattern = input()


def PatternFind(text, pattern):
    a = re.search(pattern, text)
    return re.search(pattern, text).start() if a else -1


print(PatternFind(text, pattern.replace('@', '.')))
