n = int(input())
room = list(map(int, input().split()))
room_set = set(room)
print(((sum(room_set)*n) - sum(room))//(n-1))