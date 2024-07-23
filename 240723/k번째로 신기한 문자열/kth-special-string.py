n, k, t = input().split()
n, k = int(n), int(k)
srr = []
for _ in range(n):
    s = input()
    if t in s:
        srr.append(s)
srr.sort()
print(srr[k-1])