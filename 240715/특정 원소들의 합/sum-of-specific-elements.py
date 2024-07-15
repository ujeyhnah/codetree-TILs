arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(4):
    for j in range(4):
        if j <= i:
            result += arr[i][j]
print(result)