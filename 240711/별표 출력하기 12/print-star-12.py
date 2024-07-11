n = int(input())
if n % 2 == 1 and n != 1:
    for i in range(n-1):
        for j in range(n):
            if i % 2 == 1 and j % 2 == 0:
                print(' ', end=' ')
            else:
                print('*',end = ' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            if i % 2 == 1 and j % 2 == 0:
                print(' ', end=' ')
            else:
                print('*',end = ' ')
        print()