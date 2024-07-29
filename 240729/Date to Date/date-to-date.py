m1, d1, m2, d2 = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
for m in range(m1, m2+1):
    if m1 == m2 and d1 == d2:
        result = 1
        break
    if m == m1:
        result = result + days[m-1] - d1+1
    elif m == m2:
        result = result + d2
    else:
        result += days[m-1]
print(result)