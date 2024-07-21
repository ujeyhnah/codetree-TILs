def func(n):
    if n == 1 or n == 2:
        return n
    return func(n-2) + n
n = int(input())
print(func(n))