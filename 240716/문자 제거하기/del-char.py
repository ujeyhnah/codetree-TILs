s = input()
s = list(s)
while len(s) > 1:
    x = int(input())
    if len(s) >= x:
        s.pop(x)
        print(''.join(s))
    else:
        s.pop(-1)
        print(''.join(s))
        break