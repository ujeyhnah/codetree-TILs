n, k, t = input().split()
n, k = int(n), int(k)
srr = []
for _ in range(n):
    s = input()
    if s[:len(t)] == t:
        srr.append(s)
srr.sort()
print(srr[k-1])