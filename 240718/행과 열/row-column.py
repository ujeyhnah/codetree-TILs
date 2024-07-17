a, b = map(int, input().split())
for i in range(1, a+1):
    idx = 1
    for j in range(b):
        print(idx*i,end=' ')
        idx+=1
    print()