n = int(input())
arr = list(map(int, input().split()))
chk = []
max_val = -1
for i in arr:
    if i not in chk:
        chk.append(i)
        if i > max_val:
            max_val = i
    elif i in chk and i > max_val:
        max_val = -1
print(max_val)