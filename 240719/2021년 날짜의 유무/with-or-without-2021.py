def func(m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= d <= 31:
            return True

    elif m in [4, 6, 9, 11]:
        if 1 <= d <= 30:
            return True
    
    elif m == 2:
        if 1 <= d <= 28:
            return True
    return False
m, d = map(int, input().split())
print('Yes' if func(m, d) else 'No')