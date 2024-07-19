def func(a, b):
    return max(a,b)+25, min(a,b)*2
a, b = map(int, input().split())
res1, res2 = func(a, b)
print(min(res1,res2), max(res1, res2))