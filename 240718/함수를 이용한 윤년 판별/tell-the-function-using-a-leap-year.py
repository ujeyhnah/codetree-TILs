def func(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    else:
        return False
y = int(input())
print('true' if func(y) else 'false')