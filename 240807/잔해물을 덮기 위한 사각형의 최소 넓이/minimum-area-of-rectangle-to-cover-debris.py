x1, y1, x2, y2 = map(int, input().split())
x_1, y_1, x_2, y_2 = map(int, input().split())

rect = (x2 - x1) * (y2 - y1) # 첫 번째 직사각형 넓이
ix1, iy1, ix2, iy2 = max(x1, x2), max(y1, y2), min(x_1, x_2), min(y_1, y_2) # 교집합 좌표

# 교집합 넓이
if ix1 < ix2 and iy1 < iy2:
    irect = (ix2 - ix1) * (iy2 - iy1)
else:
    irect = 0

print(rect - irect)