n, m = map(int, input().split())
coin = [[0]*n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    coin[r-1][c-1] = 1
for i in range(n):
    print(*coin[i])