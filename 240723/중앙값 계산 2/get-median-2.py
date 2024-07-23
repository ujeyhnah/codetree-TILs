n = int(input())
nrr = list(map(int, input().split()))
for i in range(len(nrr)):
    if i % 2 == 0:
        tmp = sorted(nrr[:i+1])
        print(tmp[len(tmp)//2], end=' ')