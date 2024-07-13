s1, s2 = input().split()
result1, result2 = '', ''
for c in s1:
    if '0' <= c <= '9':
        result1 += c
    else:
        break
for c in s2:
    if '0' <= c <= '9':
        result2 += c
    else:
        break
print(int(result1)+int(result2))