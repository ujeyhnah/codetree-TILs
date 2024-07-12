arr = list(map(int, input().split()))
result1, result2 = 0, []
for i in range(1, len(arr), 2):
    result1 += arr[i]
for i in range(0, len(arr), 2):
    if i != 0:
        result2.append(arr[i])
print(f'{result1} {sum(result2)/len(result2):.1f}')