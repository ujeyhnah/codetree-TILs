cnt = 0
while(True):
    x = int(input())
    if x % 2 == 1:
        continue
    else:
        print(x//2)
        cnt += 1
    if cnt == 3:
        break