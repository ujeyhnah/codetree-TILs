def isin(n):
    if '3' in str(n):
        return True
    elif '6' in str(n):
        return True
    elif '9' in str(n):
        return True
    else:
        return False
def func(a, b):
    cnt = 0
    for i in range(a, b+1):
        if isin(i) or i % 3 == 0:
            cnt += 1
    return cnt
a, b = map(int, input().split())
print(func(a,b))