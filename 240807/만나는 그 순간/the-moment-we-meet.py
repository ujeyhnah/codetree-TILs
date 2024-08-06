n, m = map(int, input().split())
arr = [0] * 2001
idx = 1
for _ in range(n):
    d, t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(idx, idx+t+1):
            arr[i] = arr[i-1]-1
        idx = i
    else:
        for i in range(idx, idx+t+1):
            arr[i] = arr[i-1]+1
        idx = i
brr = [0] * 2001
idx = 1
for _ in range(m):
    d, t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(idx, idx+t+1):
            brr[i] = brr[i-1]-1
        idx = i
    else:
        for i in range(idx, idx+t+1):
            brr[i] = brr[i-1]+1
        idx = i

result = -1
for i in range(1, len(arr)):
    if arr[i] == brr[i]:
        result = i
        break
print(result)