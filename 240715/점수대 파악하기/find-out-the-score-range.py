arr = list(map(int, input().split()))
cntrr = [0] * 10
for sc in arr:
    if sc == 0:
        break
    else:
        cntrr[sc//10-1] += 1
for i in range(len(cntrr)-1,-1, -1):
    print(f'{(i+1)*10} - {cntrr[i]}')