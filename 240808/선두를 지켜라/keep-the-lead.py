n, m = map(int, input().split())
arr = [0] * 1001
brr = [0] * 1001
idx = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(idx+1, idx+t+1):
        arr[i] = arr[i-1] + (v*t)/t
    idx = i
idx = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(idx+1, idx+t+1):
        brr[i] = brr[i-1] + (v*t)/t
    idx = i
cnt = [0]
for t in range(idx):
    if arr[t] > brr[t]:
        if cnt[-1] != 'a':
            cnt.append('a')
    elif arr[t] < brr[t]:
        if cnt[-1] != 'b':
            cnt.append('b')
print(len(cnt)-2)