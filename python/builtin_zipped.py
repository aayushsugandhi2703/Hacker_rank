inp = input().split()
N = int(inp[0])
M = int(inp[1])
a= []
for i in range(M):
    a.append(tuple(list(map(float, input().split()))))
avg = [sum(x)/M for x in zip(*a)]
# in this zip function, *a is used to unpack the list of tuples
# zip(*a) will return a list of tuples where the ith tuple contains the ith element of each of the tuples in a
# for example, if a = [(1,2,3),(4,5,6),(7,8,9)], then zip(*a) will return [(1,4,7),(2,5,8),(3,6,9)]
for i in avg:
    print(i)