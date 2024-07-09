a, b = map(int, input().split())
result, cnt = 0, 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        result += i
        cnt += 1
print(f'{result} {result/cnt:.1f}')