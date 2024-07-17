n = int(input())
idx = 0
for i in range(n):
    for j in range(i+1):
        ch = chr(ord('A')+idx)
        if 'A' <= ch <= 'Z':
            print(ch,end='')
            idx += 1
        else:
            idx = 0
            print(chr(ord('A')+idx),end='')
            idx += 1
    print()