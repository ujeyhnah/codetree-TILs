n = int(input())
idx = 1
for i in range(n):
    for j in range(n):
        if idx<1 or idx > 9:
            idx = 1
        print(idx, end='')
        idx += 1
    print()