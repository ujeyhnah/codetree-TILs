arr = list(map(int, input().split()))
result1, result2 = 0, []
idx = 0
for i in range(len(arr)):
    idx += 1
    if i % 2 == 1:
        result1 += arr[i]
    elif idx % 3 == 0:
        result2.append(arr[i])
print(f'{result1} {sum(result2)/len(result2):.1f}')