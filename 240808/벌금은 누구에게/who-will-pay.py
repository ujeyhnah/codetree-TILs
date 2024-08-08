n, m, k = map(int, input().split())
arr = [0] * (n+1)
for _ in range(m):
    x = int(input())
    arr[x] += 1
result = -1
for i in range(len(arr)):
    if arr[i] >= k:
        result = i
        break
print(result)