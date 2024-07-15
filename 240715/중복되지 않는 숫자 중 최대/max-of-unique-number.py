n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]
chk = []
for i in arr:
    if max_val < i and i not in chk:
        chk.append(i)
        max_val = i
    elif max_val < i and i in chk:
        max_val = -1
print(max_val)