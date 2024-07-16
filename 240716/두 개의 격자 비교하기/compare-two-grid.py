n, m = map(int, input().split())
arr, brr = [], []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for _ in range(n):
    brr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j] == brr[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()