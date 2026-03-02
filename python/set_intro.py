def average(array):
    total =0
    unique =set(array)
    size =len(unique)
    total=sum(unique)
    average = total/size
    return average
    

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)