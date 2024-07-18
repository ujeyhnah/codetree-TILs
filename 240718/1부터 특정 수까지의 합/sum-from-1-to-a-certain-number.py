def func(n):
    sum_val = sum([i for i in range(1, n+1)])
    return sum_val // 10
n = int(input())
print(func(n))