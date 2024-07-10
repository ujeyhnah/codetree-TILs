chk = 0
for _ in range(5):
    x = int(input())
    if x % 3 == 0:
        chk = 1
    else:
        chk = 0
print(chk)