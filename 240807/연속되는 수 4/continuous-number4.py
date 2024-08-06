arr = []
for _ in range(int(input())):
    arr.append(int(input()))

result, cnt = 1, 1
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    result = max(cnt, result)
print(result)