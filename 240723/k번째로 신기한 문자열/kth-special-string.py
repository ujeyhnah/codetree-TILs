n, k, t = input().split()
n, k = int(n), int(k)
srr = []
for _ in range(n):
    s = input()
    tmp = ''
    for i in range(len(t)):
        tmp += s[i]
    if t == tmp:
        srr.append(s)
srr.sort()
print(srr[k-1])