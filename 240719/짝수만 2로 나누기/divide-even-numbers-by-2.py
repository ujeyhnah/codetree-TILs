def func(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i]//=2

n = int(input())
arr = list(map(int, input().split()))
func(arr)
for i in arr:
    print(i, end=' ')