n = int(input())
nrr = [0] * 101
for _ in range(n):
    com = input().split()
    if com[1] == 'L':
        for i in range(int(com[0])):
            nrr[i] += 1
    elif com[1] == 'R':
        for i in range(int(com[0]), -1, -1):
            nrr[i] += 1
print(max(nrr))