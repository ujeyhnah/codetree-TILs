class Info:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

n = int(input())
people = []
for _ in range(n):
    x = input().split()
    people.append(Info(x[0], int(x[1]), int(x[2])))
people.sort(key = lambda x: (x.cm, -x.kg))
for p in people:
    print(p.name, p.cm, p.kg)