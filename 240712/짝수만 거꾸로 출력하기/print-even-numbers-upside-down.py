result = []
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        result.append(i)
print(*result[::-1])