s = ["apple", "banana", "grape", "blueberry", "orange"]
x = input()
cnt = 0
for c in s:
    if c[2] == x or c[3] == x:
        print(c)
        cnt += 1
print(cnt)