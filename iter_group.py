# this function use the itertools groupby function to group the elements of a string
# it takes a string as input and returns a list of tuples
# each tuple contains the character and the number of times it occurs in the string
# the function uses the groupby function to group the elements of the string

from itertools import groupby

s = input().strip()  

compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]

print(" ".join(f"({count}, {key})" for count, key in compressed))