def func(s, c):
    if c in s:
        return s.index(c)
    else:
        return -1
s = input()
c = input()
print(func(s, c))