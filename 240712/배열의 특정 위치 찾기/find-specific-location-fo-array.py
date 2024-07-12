arr = list(map(int, input().split()))
result1, result2 = 0, []
for i in range(1, len(arr), 2):
    result1 += arr[i]
idx = 1
for i in range(len(arr)):
    if idx % 3 == 0:
        result2.append(arr[i])
    idx += 1

print(f'{result1} {sum(result2)/len(result2):.1f}')