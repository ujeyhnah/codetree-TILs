n = int(input())
nrr = [0] * 100001
idx = 0
for _ in range(n):
    com = input().split()
    if com[1] == 'L':
        for i in range(idx - int(com[0]), idx):
            nrr[i+1000] += 1
            idx = i
    elif com[1] == 'R':
        for i in range(idx, idx+int(com[0])):
            nrr[i+1000]+= 1
            idx = i
cnt = 0
for i in range(len(nrr)):
    if nrr[i] >= 2:
        cnt += 1
print(cnt)