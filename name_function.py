#You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#Hello firstname lastname! You just delved into python.
#Function Description
#Complete the print_full_name function in the editor below.
#print_full_name has the following parameters:
#string first: the first name
#string last: the last name

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
    
first_name = input()
last_name = input()
print_full_name(first_name, last_name)