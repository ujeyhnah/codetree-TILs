s = []
for _ in range(10):
    s.append(input())
x = input()
chk = False
for i in s:
    if i[-1] == x:
        print(i)
        chk = True
if chk == False:
    print('None')