x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

checked = [[0] * 2001 for _ in range(2001)]

# 직사각형에 주어진 순으로 1, 2 번호를 붙여줍니다.
for x in range(x1_1, x2_1):
    for y in range(y1_1, y2_1):
        checked[x+1000][y+1000] = 1

for x in range(x1_2, x2_2):
    for y in range(y1_2, y2_2):
        checked[x+1000][y+1000] = 2
'''
1, 2 순으로 붙였는데도
아직 숫자 1로 남아있는 곳들 중 최대 최소 x, y 값을 전부 계산합니다.
'''

MAX_R = 2000
min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# Case 1. 첫 번째 직사각형이 전혀 남아있지 않다면 넓이는 0입니다.
if not first_rect_exist:
    area = 0
# Case 2. 첫 번째 직사각형이 남아있다면, 넓이를 계산합니다.
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)