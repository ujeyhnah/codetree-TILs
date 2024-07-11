s = input()
result = []
for i in range(len(s)):
    if i % 2 == 1:
        result.append(s[i])
result.reverse()
for i in result:
    print(i,end='')