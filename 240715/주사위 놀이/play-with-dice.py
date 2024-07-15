dice = list(map(int, input().split()))
cntrr = [0] * 6
for i in dice:
    cntrr[i-1] += 1
for i in range(len(cntrr)):
    print(f'{i+1} - {cntrr[i]}')