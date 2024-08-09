N, K, P, T = map(int, input().split())
prr = [[0, K] for _ in range(N+1)]
prr[P] = [1, K]
timelist = [[0,0] for _ in range(1001)]
for _ in range(T):
    t, x, y = map(int, input().split())
    timelist[t] = [x, y]
for hand in timelist:
    if hand[0] > 0 and hand[1] > 0:
        x, y = hand[0], hand[1]
        if prr[x][0] == 1 and (1 <= prr[x][1] <= K):
            prr[y][0] = 1
            prr[x][1] -= 1
        elif prr[y][0] == 1 and (1 <= prr[y][1] <= K):
            prr[x][0] = 1
            prr[y][1] -= 1

for x in range(1, len(prr)):
    print(prr[x][0], end='')