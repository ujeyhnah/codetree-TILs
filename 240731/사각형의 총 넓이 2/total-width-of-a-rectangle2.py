n = int(input())
arr = [[0]*201 for _ in range(201)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i+100][j+100] == 0:
                arr[i+100][j+100] = 1
cnt = 0
for i in range(len(arr)):
    cnt += arr[i].count(1)
print(cnt)