a, b, c = map(int, input().split())
w = 11*1440 + 11 * 60 + 11
r = a*1440 + b * 60 + c
if w > r:
    print(-1)
else:
    print(r-w)