import collections
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize

text = open('input.txt', 'r').read()
stopwords = open('stop.txt', 'r').read()

# deleting punctuation
tokenizer = RegexpTokenizer(r'\w+')
# dividing into sentences
sentences = sent_tokenize(text)
# dividing into words
words = tokenizer.tokenize(text)

# accumulators for all word and sentences length
allWordLen = 0
allSentLen = 0

# storage for keeping words with their lengths
# we need storage to print how many max/min words we want
wordLenCnt = {}

# iterating over words
for word in words:
    w = word.lower().replace('_', '').replace("'", '')
    if w not in stopwords and not w.isdigit():
        if w not in wordLenCnt:
            wordLenCnt[w] = len(w)
    allWordLen += len(w)

# iterating over sentences
for snt in sentences:
    allSentLen += len(snt)

# sorting {word: count} storage
resByWords = sorted(collections.Counter(wordLenCnt).most_common(),
                    key=lambda l: l[1], reverse=True)

# computing average word and sentences length
average = allWordLen / len(words)
averageSent = allSentLen / len(sentences)

# printing result
print(f'Average word length - {average}')
print(f'Average sentences length - {averageSent}')
print(f'Word with max symbols - {resByWords[:10]}')
print(f'Word with min symbols - {resByWords[-10:]}')
