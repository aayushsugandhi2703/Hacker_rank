# The function used here is itertools.permutation() which is used to generate all possible permutations of an iterable.
# The permutation() function takes two arguments:
# iterable: The iterable for which the permutations are to be generated.
# r: The number of elements in each permutation.
# The permutation() function returns an iterator containing all possible permutations.

from itertools import permutations

# Taking input
s = input().upper().split()
result = list(permutations(s[0],int(s[1])))
for i in sorted(result):
    print("".join(i))

# this will print result in sorted order