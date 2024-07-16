s, q = input().split()
for _ in range(int(q)):
    x = int(input())
    if x == 1:
        s = s[1:] + s[0]
    elif x == 2:
        s = s[-1] + s[:-1]
    else:
        ts = list(s)
        for i in range(len(ts)//2):
            ts[i], ts[len(ts)-i-1] = ts[len(ts)-i-1], ts[i]
        s = ''.join(ts)
    print(s)