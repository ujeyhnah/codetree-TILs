def func(a, b):
    if a > b:
        return a+25, b*2
    else:
        return a*2, b+25
a, b = map(int, input().split())
a, b = func(a, b)
print(a, b)