s = input()
s1, s2 = s[0], s[1]
result = ''
for c in s:
    if c == s1:
        result += s2
    elif c == s2:
        result += s1
    else:
        result += c
print(result)