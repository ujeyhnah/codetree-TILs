class Info:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

people = []
for _ in range(5):
    x = input().split()
    people.append(Info(x[0], int(x[1]), float(x[2])))

print('name')
people.sort(key = lambda x: x.name)
for p in people:
    print(f'{p.name} {p.cm} {p.kg:.1f}')
print('\nheight')
people.sort(key = lambda x: -x.cm)
for p in people:
    print(f'{p.name} {p.cm} {p.kg:.1f}')