arr = list(map(int, input().split()))
try:
    x = arr.index(0, 1)
except:
    x = len(arr)
nrr = arr[:x]
print(f'{sum(nrr)} {sum(nrr)/len(nrr):.1f}')