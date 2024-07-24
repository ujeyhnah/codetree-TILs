class Location:
    def __init__(self, name, num, reg):
        self.name = name
        self.num = num
        self.reg = reg

n = int(input())
neigs = []
for _ in range(n):
    x = input().split()
    neigs.append(Location(x[0],x[1],x[2]))
for i in range(n-1):
    if neigs[i].name > neigs[i+1].name:
        neigs[i], neigs[i+1] = neigs[i+1], neigs[i]

print(f'name {neigs[-1].name}')
print(f'addr {neigs[-1].num}')
print(f'city {neigs[-1].reg}')