#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Find the maximum height among the letters in the word
    # ord(c) - ord('a') gives the index of character c in the alphabet (0 for 'a', 1 for 'b', ..., 25 for 'z')
    # h[ord(c) - ord('a')] fetches the height of that character from the list h
    maximum = max(h[ord(i)-ord('a')] for i in word)
    area = maximum * len(word)
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
