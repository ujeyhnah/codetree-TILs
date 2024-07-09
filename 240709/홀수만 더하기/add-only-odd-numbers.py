n = int(input())
result = 0
for _ in range(n):
    x = int(input())
    if x % 2 == 1 and x % 3 == 0:
        result += x
print(result)