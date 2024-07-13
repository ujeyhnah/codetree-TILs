s1 = input()
s2 = input()
i1, i2 = '', ''
for c in s1:
    if '0'<=c<='9':
        i1 += c
for c in s2:
    if '0'<=c<='9':
        i2 += c
print(int(i1)+int(i2))