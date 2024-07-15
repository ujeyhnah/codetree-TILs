n = int(input())
arr = list(map(int, input().split()))
f = arr[0]
while True:
    x = arr.index(max(arr),1)
    print(x+1, end=' ')
    arr = arr[:x]
    if f == max(arr):
        print(1)
        break