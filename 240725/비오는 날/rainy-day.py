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
for i in range(len(rains)-1):
    if rains[i].day < rains[i].day:
        rains[i], rains[i+1] = rains[i+1], rains[i]
print(rains[0].day, rains[0].week, rains[0].whe)