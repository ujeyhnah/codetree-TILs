n = int(input())
rect = [[0] * 201 for _ in range(201)]
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if i % 2 == 0: # red = 1
        for x in range(x1, x2):
            for y in range(y1, y2):
                rect[x+100][y+100] = 1
    else: # blue = 2
        for x in range(x1, x2):
            for y in range(y1, y2):
                rect[x+100][y+100] = 2

blue = 0
for x in range(len(rect)):
    blue += rect[x].count(2)
print(blue)