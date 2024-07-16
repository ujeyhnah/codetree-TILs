s = input()
n = int(input())
cnt = 0
for c in range(len(s)-1, -1, -1):
    print(s[c],end='')
    cnt += 1
    if cnt == n:
        break