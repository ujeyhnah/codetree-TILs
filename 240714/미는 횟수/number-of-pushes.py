A = input()
B = input()
chk = False
for i in range(1, len(A)+1):
    A = A[-1] + A[:-1]
    if A == B:
        print(i)
        chk = True
        break
if chk == False:
    print(-1)