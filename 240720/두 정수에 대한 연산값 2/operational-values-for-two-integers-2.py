def func(n, m):
    if n > m:
        return n*2, m+10
    else:
        return n+10, m*2
a, b = map(int, input().split())
a, b = func(a, b)
print(a, b)