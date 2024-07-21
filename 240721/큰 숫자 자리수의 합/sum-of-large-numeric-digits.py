a, b, c = map(int, input().split())
mul_val = a*b*c

def func(n):
    if n == 0:
        return n
    return n%10 + func(n//10)
print(func(mul_val))