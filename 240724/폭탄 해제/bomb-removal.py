class bomb:
    def __init__(self, cod, col, sec):
        self.cod = cod
        self.col = col
        self.sec = sec

x = input().split()
b = bomb(x[0],x[1],x[2])
print(f'code : {b.cod}')
print(f'color : {b.col}')
print(f'second : {b.sec}')