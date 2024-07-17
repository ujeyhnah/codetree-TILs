n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
idx = 1
for i in range(n + m - 1):
    if i < m:
        r = 0
        c = i
    else:
        r = i - m + 1
        c = m - 1
    while r < n and c >= 0:
        arr[r][c] = idx
        idx += 1
        r += 1
        c -= 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()