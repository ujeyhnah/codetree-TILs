n = int(input())
for i in range(n):
    for k in range(n-i):
        print('*',end='')
    for j in range(i*2):
        print(' ',end='')
    for q in range(n-i):
        print('*',end='')
    print()