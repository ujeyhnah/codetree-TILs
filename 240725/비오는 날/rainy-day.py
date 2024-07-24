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
    if int(rains[i].day[:4]) == int(rains[i].day[:4]):
        if int(rains[i].day[5:7])==int(rains[i].day[5:7]):
            if int(rains[i].day[8:10]) > int(rains[i+1].day[8:10]):
                rains[i], rains[i+1] = rains[i+1], rains[i]
        if int(rains[i].day[5:7]) > int(rains[i+1].day[5:7]):
            rains[i], rains[i+1] = rains[i+1], rains[i]
    if int(rains[i].day[:4]) > int(rains[i+1].day[:4]):
        rains[i], rains[i+1] = rains[i+1], rains[i]

print(rains[0].day, rains[0].week, rains[0].whe)