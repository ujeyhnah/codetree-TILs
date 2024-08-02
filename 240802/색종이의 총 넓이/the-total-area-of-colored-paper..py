n = int(input())
arr = [[0]*1001 for _ in range(1001)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+8):
        for j in range(x, x+8):
            if arr[i][j] == 0:
                arr[i][j] = 1
cnt = 0
for i in range(len(arr)):
    cnt += arr[i].count(1)
print(cnt)