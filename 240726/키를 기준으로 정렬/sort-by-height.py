class People:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

n = int(input())
p = []
for _ in range(n):
    x = input().split()
    p.append(People(x[0], int(x[1]), x[2]))

p.sort(key=lambda x: x.cm)
for i in range(n):
    print(p[i].name, p[i].cm, p[i].kg)