n = int(input())
arr = list(map(int, input().split()))
chk = [0] * (max(arr)+1)
for i in arr:
    chk[i] += 1
while True:
    if len(chk) == 0:
        print(-1)
        break
    if chk[max(arr)] == 1:
        print(max(arr))
        break
    else:
        chk.remove(max(arr))