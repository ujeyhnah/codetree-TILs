arr = []
for _ in range(int(input())):
    co = input().split()
    if len(co) == 2:
        a = int(co[1])
    if co[0] == 'push_front':
        arr.insert(0, a)
    elif co[0] == 'push_back':
        arr.append(a)
    elif co[0] == 'pop_front':
        print(arr.pop(0))
    elif co[0] == 'pop_back':
        print(arr.pop())
    elif co[0] == 'size':
        print(len(arr))
    elif co[0] == 'empty':
        print(1 if len(arr) == 0 else 0)
    elif co[0] == 'front':
        print(arr[0])
    elif co[0] == 'back':
        print(arr[-1])