n = int(input())
idx = 1
for i in range(n):
    for j in range(i+1):
        print(idx, end=' ')
        idx += 1
    print()