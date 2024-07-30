n = input()
result = 0
for i in n:
    result = result * 2 + int(i)
result *= 17
digits = []
while True:
    if result < 2:
        digits.append(result)
        break
    digits.append(result%2)
    result//=2
for x in digits[::-1]:
    print(x, end='')