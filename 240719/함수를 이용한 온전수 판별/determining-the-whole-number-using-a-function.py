def cond1(n):
    if n % 2 == 0:
        return False
    else:
        return True

def cond2(n):
    if n%10 == 5:
        return False
    else:
        return True

def cond3(n):
    if n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True

def func(a, b):
    cnt = 0
    for i in range(a, b+1):
        if cond1(i) and cond2(i) and cond3(i):
            cnt += 1
    return cnt

a, b = map(int, input().split())
print(func(a, b))