s = input()
result = 0
for i in s:
    if '0'<=i<='9':
        result+=int(i)
print(result)