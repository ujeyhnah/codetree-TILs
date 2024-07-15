cntrr = [0] * 4
for _ in range(3):
    co, tmp = input().split()
    tmp = int(tmp)
    if co == 'Y' and tmp >= 37:
        cntrr[0] += 1
    elif co == 'N' and tmp >= 37:
        cntrr[1] += 1
    elif co == 'Y' and tmp < 37:
        cntrr[2] += 1
    else:
        cntrr[3] += 1
print(*cntrr, end=' ')
print('E' if cntrr[0] >= 2 else '')