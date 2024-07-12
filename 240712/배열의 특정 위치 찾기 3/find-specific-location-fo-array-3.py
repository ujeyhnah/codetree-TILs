arr = list(map(int, input().split()))
x = arr.index(0, 1)
nrr = arr[:x]
print(nrr[-3]+nrr[-2]+nrr[-1])