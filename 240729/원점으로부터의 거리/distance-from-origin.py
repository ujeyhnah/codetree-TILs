class Pos:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
n = int(input())
pos = []
for i in range(n):
    x = input().split()
    pos.append(Pos(int(x[0]), int(x[1]), i+1))
pos.sort(key = lambda x: -(abs(0-x.x) - abs(0-x.y)))
for po in pos:
    print(po.idx)