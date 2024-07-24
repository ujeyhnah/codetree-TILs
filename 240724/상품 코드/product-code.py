class product:
    def __init__(self, name='codetree', code='50'):
        self.name = name
        self.code = code

x = input().split()
p1 = product(x[0],x[1])
p2 = product()
print(f'product {p2.code} is {p2.name}')
print(f'product {p1.code} is {p1.name}')