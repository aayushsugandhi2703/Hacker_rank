n = int(input())
s = set(map(int, input().split()))
nos = int(input())
for i in range(nos):
    str =input().split()
    set1 = set(map(int, input().split()))
    if str[0] == 'intersection_update':
        s.intersection_update(set1)
    elif str[0] == 'update':
        s.update(set1)
    elif str[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(set1)
    elif str[0] == 'difference_update':
        s.difference_update(set1)
print(sum(s))