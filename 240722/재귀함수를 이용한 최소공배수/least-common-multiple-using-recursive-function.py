n = int(input())
nrr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def func(n):
    if n == 1:
        return nrr[0]
    return lcm(nrr[n-1], func(n-1))

print(func(n))