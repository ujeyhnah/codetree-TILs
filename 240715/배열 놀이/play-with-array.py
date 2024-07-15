n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    co = list(map(int, input().split()))
    if co[0] == 1:
        print(arr[co[1]-1])
    elif co[0] == 2:
        if co[1] in arr:
            print(arr.index(co[1])+1)
        else:
            print(0)
    elif co[0] == 3:
        print(*arr[co[1]-1:co[2]])