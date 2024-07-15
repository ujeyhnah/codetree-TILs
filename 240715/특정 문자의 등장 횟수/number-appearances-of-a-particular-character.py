s = input()
r1, r2 = 0, 0
for i in range(len(s)-1):
    if s[i]+s[i+1] == 'ee':
        r1 += 1
    if s[i]+s[i+1] == 'eb':
        r2 += 1
print(r1, r2)