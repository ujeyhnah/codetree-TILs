n, k = map(int, input().split())
blocks = [0] * (n+1)
for _ in range(k):
    i, j = map(int, input().split())
    for x in range(i, j+1):
        blocks[x] += 1
print(max(blocks))