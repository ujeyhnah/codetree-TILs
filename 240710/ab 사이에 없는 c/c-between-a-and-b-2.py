a, b, c = map(int, input().split())
chk = 0
for i in range(a, b+1):
    if i % c == 0:
        chk = 1
        break
print('NO' if chk == 1 else 'YES')