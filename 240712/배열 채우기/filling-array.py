arr = list(map(int, input().split()))
try:
    x = arr.index(0, 1)
except:
    pass
nrr = arr[:x]
print(*nrr[::-1])