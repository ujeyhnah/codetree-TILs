def week(m, d):
    day_of_week = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = d
    for i in range(1, m):
        total += day_of_week[i]

    return total

m1, d1, m2, d2 = map(int, input().split())
A = input()
total1 = week(m1, d1)
total2 = week(m2, d2)

total3 = total2 - total1 + 1
week_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


cnt = total3 // 7
idx = week_name.index(A)

if idx + 1 <= (total3 % 7):
    cnt += 1
print(cnt)