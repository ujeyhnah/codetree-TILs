n = int(input())
arr = list(map(int, input().split()))
m = min(arr)
while len(arr) > 0:
    if max(arr) == m:
        print(1)
        break
    else:
        x = arr.index(max(arr), 1)
        print(x+1, end=' ')
        arr = arr[:x]