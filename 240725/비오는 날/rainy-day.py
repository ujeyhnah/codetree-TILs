import datetime
class Whether:
    def __init__(self, day, week, whe):
        self.day = day
        self.week = week
        self.whe = whe

whethers = []
n = int(input())
for _ in range(n):
    x = input().split()
    whethers.append(Whether(x[0],x[1],x[2]))
rains = []
for i in range(n):
    if whethers[i].whe == 'Rain':
        rains.append(whethers[i])
tmp_rains = sorted(rains, key=lambda x: x.day)
print(tmp_rains[0].day, tmp_rains[0].week, tmp_rains[0].whe)