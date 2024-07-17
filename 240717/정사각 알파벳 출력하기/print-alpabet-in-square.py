n = int(input())
idx = 0
for i in range(n):
    for j in range(n):
        print(chr(ord('A')+idx),end='')
        idx+=1
    print()