n = int(input())
r1, r2 = 0, 0
for _ in range(n):
    s = input()
    r1 += len(s)
    if s[0] == 'a':
        r2 += 1
print(r1, r2)