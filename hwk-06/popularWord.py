import collections

a = input()
str = []

while a != '':
    str.append(a)
    a = input()

text = '\n'.join(str)


def popularWords(text):
    wordcount = {}

    for word in text.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    if (len(wordcount) == 1):
        first, = collections.Counter(wordcount).most_common(1)
        return first[0]

    first, sec = sorted(collections.Counter(wordcount).most_common(2),
                        key=lambda l: l[1], reverse=True)

    return '---' if first[1] == sec[1] else first[0]


print(popularWords(text))
