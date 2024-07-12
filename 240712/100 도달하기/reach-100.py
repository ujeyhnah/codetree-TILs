n = int(input())
arr = [1, n]
i = 2
while True:
    x = arr[i-1]+arr[i-2]
    arr.append(x)
    if x > 100:
        break
    i += 1
print(*arr)