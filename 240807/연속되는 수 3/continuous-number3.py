n = int(input())
neg, pos = 0, 0
cnt_n, cnt_p = 0, 0
chk_n, chk_p = False, False
for _ in range(n):
    x = int(input())
    if x > 0:
        cnt_p += 1
        chk_n = False
        chk_p = True
    else:
        cnt_n += 1
        chk_p = False
        chk_n = True
    if chk_n:
        neg = max(neg, cnt_n)
        cnt_p = 0
    if chk_p:
        pos = max(pos, cnt_p)
        cnt_n = 0

print(max(neg, pos))