n = int(input())
nrr = [0] * 1001
for _ in range(n):
    com = input().split()
    if com[1] == 'L':
        for i in range(int(com[0])+100):
            nrr[i] += 1
    elif com[1] == 'R':
        for i in range(int(com[0])+100, -1, -1):
            nrr[i] += 1
print(max(nrr))