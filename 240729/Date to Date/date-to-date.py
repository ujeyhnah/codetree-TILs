m1, d1, m2, d2 = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
if m1 == m2:
    for d in range(d1, d2+1):
        result += 1
else:
    for m in range(m1, m2+1):
        if m == m1:
            result = result + days[m1-1] - d1 + 1
        elif m == m2:
            result += d2
        else:
            result += days[m-1]
print(result)