class Secret:
    def __init__(self, code, loc, time):
        self.code = code
        self.loc = loc
        self.time = time

c, l, t = input().split()
x = Secret(c, l, t)
print(f'secret code : {x.code}')
print(f'meeting point : {x.loc}')
print(f'time : {x.time}')