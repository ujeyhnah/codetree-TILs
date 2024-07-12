arr = list(map(int, input().split()))
x = arr.index(0, 1)
nrr = arr[:x]
print(nrr[0]+nrr[1]+nrr[2])