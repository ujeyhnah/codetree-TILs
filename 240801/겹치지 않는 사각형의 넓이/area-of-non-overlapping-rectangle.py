nrr = [[0]*2001 for _ in range(2001)]
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            nrr[i][j] += 1
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        if nrr[i][j]==1:
            nrr[i][j] = 0
cnt = 0
for i in range(len(nrr)):
    cnt += nrr[i].count(1)
print(cnt)