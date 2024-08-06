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
        result = max(cnt, result)
        cnt = 1
print(result)