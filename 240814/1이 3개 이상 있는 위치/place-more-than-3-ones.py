def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

result = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)