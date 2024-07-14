def whether(m):
    if 3<=m<=5:
        return 'Spring'
    elif 6<=m<=8:
        return 'Summer'
    elif 9<=m<=11:
        return 'Fall'
    elif m == 12 or m == 1 or m ==2:
        return 'Winter'
    return -1

def func(y, m, d):
    if (y % 4 == 0) or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= d <= 31:
                return whether(m)
        elif m in [4, 6, 9, 11]:
            if 1 <= d <= 30:
                return whether(m)
        elif m == 2:
            if 1 <= d <= 29:
                return whether(m)
        else:
            return -1
    else:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= d <= 31:
                return whether(m)
        elif m in [4, 6, 9, 11]:
            if 1 <= d <= 30:
                return whether(m)
        elif m == 2:
            if 1 <= d <= 28:
                return whether(m)
        else:
            return -1
    return -1

Y, M, D = map(int, input().split())
print(func(Y,M,D))