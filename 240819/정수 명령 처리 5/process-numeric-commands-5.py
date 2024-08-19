arr = []
for _ in range(int(input())):
    co = input().split()
    if co[0] == 'push_back':
        a = int(co[1])
        arr.append(a)
    elif co[0] == 'pop_back':
        arr.pop()
    elif co[0] == 'size':
        print(len(arr))
    elif co[0] == 'get':
        k = int(co[1])
        print(arr[k-1])