arr = list(map(int, input().split()))
x = arr.index(0, 1)
nrr = arr[:x]
nrr.reverse()
print(*nrr)