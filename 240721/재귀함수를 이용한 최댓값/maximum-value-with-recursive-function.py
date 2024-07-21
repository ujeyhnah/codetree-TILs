n = int(input())
nrr = list(map(int, input().split()))

def func(n):
    if n == 0:
        return nrr[0]
    return max(func(n-1), nrr[n])

print(func(n-1))