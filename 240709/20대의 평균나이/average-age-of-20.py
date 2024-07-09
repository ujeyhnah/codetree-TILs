result, cnt = 0, 0
while True:
    age = int(input())
    if 20 <= age < 30:
        result += age
        cnt += 1
    else:
        break
print(f'{result/cnt:.2f}')