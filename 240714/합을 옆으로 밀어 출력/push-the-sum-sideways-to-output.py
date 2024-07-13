result = 0
for _ in range(int(input())):
    result += int(input())
result = str(result)
print(result[1:]+result[0])