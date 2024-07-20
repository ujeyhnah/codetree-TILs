def func(n):
    if n == 1:
        return 1
    return func(n-1) + n
n = int(input())
print(func(n))