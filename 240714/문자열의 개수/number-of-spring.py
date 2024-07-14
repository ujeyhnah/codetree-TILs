srr = []
idx = 1
while True:
    s = input()
    if s == '0':
        break
    else:
        if idx % 2 == 1:
            srr.append(s)
        idx += 1
print(idx-1)
for s in srr:
    print(s)