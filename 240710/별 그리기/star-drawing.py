n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i*2+1):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for k in range(n*2-(i*2+3)):
        print('*', end='')
    print()