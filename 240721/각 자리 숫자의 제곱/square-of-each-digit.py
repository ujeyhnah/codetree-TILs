def func(n):
    if n < 10:
        return pow(n, 2)
    return func(n // 10) + (pow(n%10, 2))
n = int(input())
print(func(n))