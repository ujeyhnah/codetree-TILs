class Sn:
    def __init__(self, m, idx):
        self.m = m
        self. idx = idx
n = int(input())
numbers = list(map(int, input().split()))
sn = []
for k, num in enumerate(numbers):
    sn.append(Sn(num, k))
sn.sort(key = lambda x: x.m)
for i in range(n):
    cnt = 1
    for s in sn:
        if numbers[i]==s.m and i == s.idx:
            print(cnt, end=' ')
        cnt+=1