import re
pattern = r'^([789]{1})([0-9]{9})$'

def checking(phone):
    for i in phone:
        result = re.match(pattern, i )
        if result:
            print ("YES")
        else:
            print("NO")

if __name__ == "__main__":
    n= int(input())
    a = []
    for _ in range(n):
        ph = input()
        a.append(ph)
    checking(a)

'''
explaination for regex pattern:
^ - Asserts the start of the string
([789]{1}) - Matches a single digit that is either 7, 8, or 9
([0-9]{9}) - Matches exactly 9 digits (0-9)
$ - Asserts the end of the string
'''