arr = list(map(int, input().split()))
cnt, sum_val = 0, 0
for i in arr:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            cnt += 1
            sum_val += i
print(cnt, sum_val)