n = int(input())
nrr = list(map(int, input().split()))
for i in range(len(nrr)):
    if i % 2 == 0:
        print(nrr[i//2], end=' ')