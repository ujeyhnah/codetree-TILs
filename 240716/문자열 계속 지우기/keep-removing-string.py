a = input()
b = input()
while b in a:
    a = a.replace(b,'')
print(a)