def cond1(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def cond2(n):
    result = 0
    while n > 0:
        result += n%10
        n //= 10
    if result % 2 == 0:
        return True
    return False
def func(a, b):
    cnt = 0
    for i in range(a, b+1):
        if cond1(i) and cond2(i):
            cnt += 1
    return cnt

a, b = map(int, input().split())
print(func(a,b))