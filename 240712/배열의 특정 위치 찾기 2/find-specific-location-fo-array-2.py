arr = list(map(int, input().split()))
odd, even = sum(arr[0:len(arr):2]), sum(arr[1:len(arr):2])
print(abs(odd-even))