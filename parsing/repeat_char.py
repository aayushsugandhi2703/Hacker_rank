import re 
def validate(characters):
    match = re.search(r'([a-zA-Z0-9])\1', characters)
    if match:
        return match.group(1)
    return -1

if __name__ == '__main__' :
    string = input()
    print(validate(string))

'''
explaination for regex pattern:

([a-zA-Z0-9]) - captures any alphanumeric character and stores it in a group (group 1)
\1 - refers back to the first capturing group, checking if the same character appears immediately after it
'''