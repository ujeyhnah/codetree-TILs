x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())
for _ in range(n):
    loc, dist = input().split()
    dist = int(dist)
    if loc == 'E':
        for _ in range(dist):
            x, y = x + dx[0], y + dy[0]
    elif loc == 'S':
        for _ in range(dist):
            x, y = x + dx[1], y + dy[1]
    elif loc == 'W':
        for _ in range(dist):
            x, y = x + dx[2], y + dy[2]
    elif loc == 'N':
        for _ in range(dist):
            x, y = x + dx[3], y + dy[3]
print(x, y)