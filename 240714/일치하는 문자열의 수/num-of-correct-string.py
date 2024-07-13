n, A = input().split()
cnt = 0
for _ in range(int(n)):
    x = input()
    if A == x:
        cnt += 1
print(cnt)