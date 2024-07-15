arr = input().split()
cntrr = [0] * 9
for x in arr:
    if x == '0':
        break
    else:
        if x[0] != '0' and len(x) == 2:
            cntrr[int(x[0])-1] += 1
for i in range(len(cntrr)):
    print(f'{i+1} - {cntrr[i]}')