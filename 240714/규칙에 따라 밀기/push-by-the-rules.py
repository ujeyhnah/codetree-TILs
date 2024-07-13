A = input()
com = input()
for co in com:
    if co == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)