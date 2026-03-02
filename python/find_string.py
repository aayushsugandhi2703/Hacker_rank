# in this problem we have to find the number of occurance of a sub_string in a given string
def count_string(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count
string = input().strip()
sub_string = input().strip()
print(count_string(string, sub_string))