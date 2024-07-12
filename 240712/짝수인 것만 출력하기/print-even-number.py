n = int(input())
arr = list(map(int, input().split()))
nrr = []
for i in arr:
    if i % 2 == 0:
        nrr.append(i)
print(*nrr)