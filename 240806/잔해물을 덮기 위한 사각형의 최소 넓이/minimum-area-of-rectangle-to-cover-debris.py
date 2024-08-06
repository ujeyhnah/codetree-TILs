arr = [[0]*2001 for _ in range(2001)]
x1, y1, x2, y2 = map(int, input().split())
for i in range(y1, y2+1):
    for j in range(x1, x2+1):
        arr[i+1000][j+1000] = 1
x1, y1, x2, y2 = map(int, input().split())
for i in range(y1, y2+1):
    for j in range(x1, x2+1):
        arr[i+1000][j+1000] = 0
max_x = 0
list_y = []
for i in range(len(arr)):
    cnt_x = 0
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            cnt_x += 1
            if i not in list_y:
                list_y.append(i)
    if cnt_x > max_x:
        max_x = cnt_x
print((list_y[-1] - list_y[0]) * (max_x-1))