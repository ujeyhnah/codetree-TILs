arr = list(map(int, input().split()))
result = [chr(i) for i in arr]
print(*result)