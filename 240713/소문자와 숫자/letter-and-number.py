s = input().lower()
for i in s:
    if ord('0')<=ord(i)<=ord('9') or 'a'<=i<='z':
        print(i,end='')