n, m = map(int, input().split())
arr, brr = [], []
for _ in range(4):
    arr.append(list(map(int, input().split())))
for _ in range(4):
    brr.append(list(map(int, input().split())))
for i in range(4):
    for j in range(4):
        if arr[i][j] == brr[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()