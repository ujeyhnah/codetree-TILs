n, m = map(int, input().split())
arr = [0] * 1000001
brr = [0] * 1000001
idx = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)
    if d == 'L':
        for i in range(idx+1, idx+t+1):
            arr[i] = arr[i-1] - 1
    else:
        for i in range(idx+1, idx+t+1):
            arr[i] = arr[i-1] + 1
    idx = i
idx = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)
    if d == 'L':
        for i in range(idx+1, idx+t+1):
            brr[i] = brr[i-1] - 1
    else:
        for i in range(idx+1, idx+t+1):
            brr[i] = brr[i-1] + 1
    idx = i
cnt = 0
for t in range(1, len(arr)):
    if arr[t-1] != brr[t-1] and arr[t] == brr[t]:
        cnt += 1
print(cnt)