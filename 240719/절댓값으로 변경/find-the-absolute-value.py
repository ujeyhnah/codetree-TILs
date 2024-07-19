def absarr(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

n = int(input())
arr = list(map(int, input().split()))
absarr(arr)
print(*arr)