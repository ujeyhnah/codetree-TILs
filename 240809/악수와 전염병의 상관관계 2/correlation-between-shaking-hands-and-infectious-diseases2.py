N, K, P, T = map(int, input().split())
prr = [0] * (N+1)
prr[P] = 1
timelist = [[0,0] for _ in range(501)]
for _ in range(T):
    t, x, y = map(int, input().split())
    timelist[t] = [x, y]
for hand in timelist:
    if hand[0] > 0 and hand[1] > 0:
        x, y = hand[0], hand[1]
        if prr[x] == 1 or prr[y] == 1:
            prr[x], prr[y] = 1, 1
            K -= 1
    if K == 0:
        break
for x in range(1, len(prr)):
    print(prr[x], end='')