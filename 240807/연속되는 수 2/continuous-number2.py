n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
result = 1
cnt = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    result = max(cnt, result)
print(result)