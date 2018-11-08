import nltk
import collections
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

wordcount = {}
tokenizer = RegexpTokenizer(r'\w+')
wordnet_lemmatizer = WordNetLemmatizer()

text = open('input.txt', 'r').read()
stopwords = open('stop.txt', 'r').read()
output = open('output-v2.txt', 'w')

words = tokenizer.tokenize(text)

for word in words:
    w = wordnet_lemmatizer.lemmatize(word).lower().replace('_', '')
    if w not in stopwords:
        if w not in wordcount:
            wordcount[w] = 1
        else:
            wordcount[w] += 1

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
