start, end = map(int, input().split())
cnt = 0
for n in range(start, end+1):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += 1
    if result == 3:
        cnt += 1
print(cnt)