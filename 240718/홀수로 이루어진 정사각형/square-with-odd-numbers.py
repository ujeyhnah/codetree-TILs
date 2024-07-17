n = int(input())
idx = 11
x = 2
for i in range(n):
    idx = 11 + (x*i)
    for j in range(n):
        print(idx, end=' ')
        idx += 2
    print()