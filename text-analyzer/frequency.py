import collections

text = open('input.txt', 'r').read()
stopwords = open('stop.txt', 'r').read()
output = open('output.txt', 'w')

wordcount = {}

for word in text.lower().split():
    word = word.replace(".", "")
    word = word.replace("--", " ")
    word = word.replace(",", "")
    word = word.replace("_", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("â€œ", "")
    word = word.replace("â€˜", "")
    word = word.replace("”", "")
    word = word.replace(";", "")
    word = word.replace("“", "")
    word = word.replace("*", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

res = sorted(collections.Counter(wordcount).most_common(),
             key=lambda l: l[1], reverse=True)

bottom = '\n\nTop-25 rare words: \n\n'
top = '\n\nTop-25 words: \n\n'

for (w, c) in res[:25]:
    top += f'{w}: {c} \n'

for (w, c) in res[-25:]:
    bottom += f'{w}: {c} \n'

output.write(f'{bottom}')
output.write(f'{top} \n')
