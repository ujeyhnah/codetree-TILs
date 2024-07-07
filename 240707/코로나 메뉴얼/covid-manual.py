a_flu, a_temp = input().split()
b_flu, b_temp = input().split()
c_flu, c_temp = input().split()
cnt = 0
if a_flu == 'Y' and int(a_temp) >= 37:
    cnt += 1
if b_flu == 'Y' and int(b_temp) >= 37:
    cnt += 1
if c_flu == 'Y' and int(c_temp) >= 37:
    cnt += 1
print('E' if cnt >= 2 else 'N')