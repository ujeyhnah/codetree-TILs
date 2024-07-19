def func(a, b):
    a, b = b, a
    return a, b
n, m = map(int, input().split())
n, m = func(n, m)
print(n, m)