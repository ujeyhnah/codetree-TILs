arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))
for i in range(2):
    print(f'{sum(arr[i])/len(arr[i]):.1f}', end=' ')
print()

for i in range(4):
    sum_val = 0
    for j in range(2):
        sum_val += arr[j][i]
    print(f'{sum_val/2:.1f}', end=' ')
print()

sum_val = 0
for i in range(2):
    sum_val += sum(arr[i])
print(f'{sum_val/8:.1f}')