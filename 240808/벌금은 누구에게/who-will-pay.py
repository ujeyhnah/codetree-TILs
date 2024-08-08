n, m, k = map(int, input().split())
arr = [0] * (n+1)
result = -1
for _ in range(m):
    x = int(input())
    arr[x] += 1
    if k in arr:
        result = arr.index(k)
        break
print(result)