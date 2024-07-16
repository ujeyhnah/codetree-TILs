s = input()
cntrr = []
arr = []
cnt = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        cntrr.append(cnt)
        cnt = 1
cntrr.append(cnt)
result = ''
x = 0
for i in range(len(cntrr)):
    x += cntrr[i]
    result += s[x-1] + str(cntrr[i])
print(len(result))
print(result)