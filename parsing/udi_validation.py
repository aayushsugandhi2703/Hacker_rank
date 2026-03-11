import re

pattern = r'(?=(?:.*[A-Z]){2})(?=(?:.*[0-9]){3})[a-zA-Z0-9]{10}'

def validate(lists):
    for s in lists:
        if len(s)==10 and len(set(s))==10:
            if re.fullmatch(pattern, s):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")

if __name__ == '__main__':
    t = int(input())
    a = []
    for i in range(t):
        s = input()
        a.append(s) 
    validate(a)


"""
explanation of regex:
(?=(?:.*[A-Z]){2})  # Positive lookahead with non-capturing groups to ensure at least 2 uppercase letters
(?=(?:.*[0-9]){3})  # Positive lookahead with non-capturing groups to ensure at least 3 digits
[a-zA-Z0-9]{10}     # Match exactly 10 alphanumeric characters
first two lookaheads ensure that the string contains at least 2 uppercase letters and 3 digits, while the final part ensures that the string is exactly 10 characters long and consists of only alphanumeric characters.
"""