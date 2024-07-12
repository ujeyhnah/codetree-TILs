arr = list(map(int, input().split()))
sum_val, cnt = 0, 0
for i in arr:
    if i < 250:
        sum_val += i
        cnt += 1
    else:
        break
print(f'{sum_val} {sum_val/cnt:.1f}')