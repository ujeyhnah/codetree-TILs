result = 0
def func(arr, m):
    global result
    result += arr[m-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
func(arr, m)
while m > 1:
    if m % 2 == 1:
        m -= 1
    else:
        m //= 2
    func(arr, m)
print(result)