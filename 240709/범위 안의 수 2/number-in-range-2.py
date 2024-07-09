result, cnt = 0, 0
for _ in range(10):
    x = int(input())
    if 0 <= x <= 200:
        result += x
        cnt += 1
print(f'{result} {result/cnt:.1f}')