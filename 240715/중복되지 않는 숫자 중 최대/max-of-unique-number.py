n = int(input())
arr = list(map(int, input().split()))
chk = []
for i in arr:
    if i not in chk:
        chk.append(i)
    else:
        chk.remove(i)
print(max(chk) if len(chk) > 0 else -1)