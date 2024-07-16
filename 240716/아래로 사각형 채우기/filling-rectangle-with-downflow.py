n = int(input())
brr = [[0]*n for i in range(n)]
idx = 1
for i in range(n):
    for j in range(n):
        brr[j][i] += idx
        idx += 1
for i in range(n):
    for j in range(n):
        print(brr[i][j], end = ' ')
    print()