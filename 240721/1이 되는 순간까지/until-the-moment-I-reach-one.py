cnt = 0
def func(n):
    global cnt
    if n == 1:
        return n
    if n % 2 == 0:
        cnt += 1
        return func(n//2)
    else:
        cnt += 1
        return func(n//3)
n = int(input())
func(n)
print(cnt)