def func(n):
    if n == 1 or n == 2:
        return n
    return func(n//3) + func(n-1)
n = int(input())
print(func(n))