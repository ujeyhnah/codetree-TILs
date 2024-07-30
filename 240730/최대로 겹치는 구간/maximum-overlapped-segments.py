n = int(input())
pos = [0] * 1001
cnt = 0
chk = 2
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2):
        pos[i+100] += 1
print(max(pos))