import re

def validate_regex(substirng):
    pattern = r'(?<=[^aeiouAEIOU])([AEIOUaeiou]{2,})(?=[^aeiouAEIOU])'
    result = re.findall(pattern, substirng)
    for item in result:
        print(item)
        
if __name__ == '__main__':
    string = input()
    validate_regex(string)


'''
explaination for regex pattern:

(?<=[^aeiouAEIOU]) - Positive lookbehind assertion that ensures the preceding character is not a vowel (both uppercase and lowercase)

([AEIOUaeiou]{2,}) - Captures a sequence of two or more vowels (both uppercase and lowercase) and stores it in a group (group 1)

(?=[^aeiouAEIOU]) - Positive lookahead assertion that ensures the following character is not a vowel (both uppercase and lowercase)

findall() function is used to find all occurrences of the pattern in the input string and returns them as a list. 

finditer() function is used to find all occurrences of the pattern in the input string and returns an iterator yielding match objects.

'''