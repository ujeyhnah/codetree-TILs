dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
com = input()
for co in com:
    if co == 'L':
        dir_num = (dir_num + 3) % 4
    elif co == 'R':
        dir_num = (dir_num + 1) % 4
    elif co == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]
print(x, y)