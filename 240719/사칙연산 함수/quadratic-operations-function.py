def calc(a, op, b):
    if op == '+':
        print(f'{a} {op} {b} = {a+b}')
    elif op == '-':
        print(f'{a} {op} {b} = {a-b}')
    elif op == '/':
        print(f'{a} {op} {b} = {a//b}')
    elif op == '*':
        print(f'{a} {op} {b} = {a*b}')
    else:
        print('False')
a, o, c = input().split()
a, c = int(a), int(c)
calc(a,o,c)