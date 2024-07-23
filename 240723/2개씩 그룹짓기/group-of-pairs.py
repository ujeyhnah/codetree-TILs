n = int(input())
nrr = list(map(int, input().split()))
nrr.sort()
result = []
l = len(nrr)
for i in range(l//2):
    result.append(nrr[i]+nrr[l-i-1])
print(max(result))