# Given an integer n and n space-separated integers, check if all the integers are non-negative and at least one of them is a palindrome.
# the code should be within 3 lines
n = input()
number_list = tuple(map(int, input().split()))
print(all(number>=0 for number in number_list) and any(str(number) == str(number)[::-1] for number in number_list))