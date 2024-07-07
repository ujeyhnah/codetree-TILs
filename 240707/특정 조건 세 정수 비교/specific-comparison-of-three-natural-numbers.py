a, b, c = map(int, input().split())
result1 = 1 if a <=b and a <= c else 0
result2 = 1 if a == b and b == c and a == c else 0
print(result1, result2)