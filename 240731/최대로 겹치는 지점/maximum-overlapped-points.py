n = int(input())
nrr = [0] * 101
for _ in range(n):
    x1, x2 = map(int, input().split())
    for x in range(x1, x2+1):
        nrr[x] += 1
print(max(nrr))