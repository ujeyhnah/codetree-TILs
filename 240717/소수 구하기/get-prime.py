n = int(input())
for i in range(2, n+1):
    chk = False
    for j in range(2, i):
        if i % j == 0:
            chk = True
            break
    if chk == False:
        print(i, end=' ')