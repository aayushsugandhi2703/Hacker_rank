# this problem is to counte the number of occurance of a word from input data
from collections import Counter
n = int(input())
words = []
counter  = Counter()

for i in range(n):
    word= input().strip()
    if word not in counter:
        words.append(word)
    counter[word] += 1

print(len(words))
print(" ".join(str(counter[word]) for word in words))
