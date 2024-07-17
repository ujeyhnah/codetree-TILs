n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
for i in range(n1):
    if arr[i] == brr[0]:
        idx = i
        break
trr = arr[i:len(brr)+i]
chk = 1
for i in range(n2):
    if trr[i] != brr[i]:
        chk = 0
        break
print('Yes' if chk==1 else 'No')