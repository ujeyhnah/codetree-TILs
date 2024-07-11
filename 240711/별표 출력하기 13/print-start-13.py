n = int(input())
p, x = 0, 1
for i in range(2*n):
    if i % 2 == 0:
        for j in range(n-p):
            print('*', end=' ')
        p+=1
    else:
        for k in range(x):
            print('*', end=' ')
        x += 1
    print()