global result
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    result = 0
    a1, a2 = map(int, input().split())
    result += sum(arr[a1-1:a2])
    print(result)