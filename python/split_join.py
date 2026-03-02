# to split and joint them back
#it will split by space and joiin them by - like a ay u : a-ay-u


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    
line = input()
result = split_and_join(line)
print(result)