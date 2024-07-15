arr = list(map(int, input().split()))
x1, x2 = [], []
for i in arr:
    if i < 500:
        x1.append(i)
    else:
        x2.append(i)
print(max(x1), min(x2))