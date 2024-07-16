s = input()
s = list(s)
while True:
    if len(s) == 1:
        break
    x = int(input())
    if len(s) >= x:
        s.pop(x)
    else:
        s.pop(-1)
    print(''.join(s))