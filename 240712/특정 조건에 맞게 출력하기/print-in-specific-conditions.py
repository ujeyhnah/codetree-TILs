arr = list(map(int, input().split()))
x = arr.index(0, 1)
nrr = arr[:x]
for i in range(len(nrr)):
    if nrr[i] % 2 == 1:
        nrr[i] += 3
    else:
        nrr[i] //= 2
print(*nrr)