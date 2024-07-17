n = int(input())
idx = 2
for i in range(n):
    for j in range(n):
        if idx > 8:
            idx = 2
        print(idx, end=' ')
        idx += 2
    print()