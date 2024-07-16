s, q = input().split()
for _ in range(int(q)):
    co = input().split()
    if co[0] == '1':
        s = list(s)
        co[1], co[2] = int(co[1]), int(co[2])
        s[co[1]-1], s[co[2]-1] = s[co[2]-1], s[co[1]-1]
        print(''.join(s))
    elif co[0] == '2':
        s = ''.join(s)
        s = s.replace(co[1], co[2])
        print(s)