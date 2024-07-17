n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
for i in range(n1):
    if arr[i] == brr[0]:
        idx = i
        break
print('Yes' if arr[i:len(brr)+i] == brr else 'No')