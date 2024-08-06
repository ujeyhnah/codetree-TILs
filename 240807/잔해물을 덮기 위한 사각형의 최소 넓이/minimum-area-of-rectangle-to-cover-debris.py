x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

rect = (x2_1 - x1_1) * (y2_1 - y1_1) # 첫 번째 직사각형 넓이
ix1, iy1, ix2, iy2 = max(x1_1, x1_2), max(y1_1, y1_2), min(x2_1, x2_2),min(y2_1, y2_2) # 교집합 좌표

# 교집합 넓이
irect = (ix2 - ix1) * (iy2 - iy1)

if (ix2 - ix1) < (x2_1 - x1_1) or (iy2 - iy1) < (y2_1 - y1_1):
    print(rect)
else:
    print(rect - irect)