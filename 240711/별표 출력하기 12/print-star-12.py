n = int(input())
for i in range(n):
    if i == 0:
        print('* ' * n)
    else:
        for j in range(i):
            print('  ', end='')
        for j in range(n - i):
            print('* ', end='')
        print()