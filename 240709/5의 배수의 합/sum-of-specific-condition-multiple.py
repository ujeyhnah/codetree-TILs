a, b = map(int, input().split())
result = 0
for i in range(min(a,b), max(a,b)+1):
    if i % 5 == 0:
        result += i
print(result)