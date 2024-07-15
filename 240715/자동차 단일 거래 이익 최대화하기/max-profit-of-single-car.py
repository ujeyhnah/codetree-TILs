n = int(input())
arr = list(map(int,input().split()))
cnr = []
for i in range(n-1):
    cnr.append(max(arr[i+1:]) - arr[i])
print(max(cnr) if max(cnr) > 0 else 0)