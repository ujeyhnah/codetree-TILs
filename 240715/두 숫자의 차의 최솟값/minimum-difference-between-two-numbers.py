n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(n):
    for j in range(i+1, n):
        result.append(arr[j]-arr[i])
print(min(result))