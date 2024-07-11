n = int(input())
p = n
for i in range(2*n):
    if i % 2 == 0:
        for j in range((i//2)+1):
            print('*', end=' ')
    else:
        for k in range(p):
            print('*', end=' ')
        p-=1
    print()