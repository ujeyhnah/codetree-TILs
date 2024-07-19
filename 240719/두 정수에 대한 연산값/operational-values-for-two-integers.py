def func(a, b):
    return min(a,b)*2, max(a,b)+25
a, b = map(int, input().split())
res1, res2 = func(a, b)
print(res1, res2)