arr = list(map(int, input().split()))
xrr = []
for i in arr:
    if i == 999 or i == -999:
        break
    else:
        xrr.append(i)
print(max(xrr), min(xrr))