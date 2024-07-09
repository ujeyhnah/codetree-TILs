n = int(input())
result, cnt = 0, 0
for _ in range(n):
    x = int(input())
    result += x
    cnt += 1
print(f'{result} {result/cnt:.1f}')