a, b = map(int, input().split())
n = input()
result = 0
for i in n:
    result = result * a + int(i)
digits = []
while True:
    if result < b:
        digits.append(result)
        break
    digits.append(result%b)
    result //= b
for x in digits[::-1]:
    print(x,end='')