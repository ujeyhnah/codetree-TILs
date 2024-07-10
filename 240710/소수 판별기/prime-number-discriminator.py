n = int(input())
chk = 0
for i in range(2, n):
    if n % i == 0:
        chk = 1
        break
print('P' if chk != 1 else 'C')