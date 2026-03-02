# in this problem we are given a string and we need to insert a character at a given position
def include(string, position,character):
    l = list(string)
    l[position]=character
    string = ''.join(l)
    return string

s = input().strip()
c = input().strip()
i = int(input().strip())
print(include(s, i, c))