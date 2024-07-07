middle, final = map(int, input().split())
scholarship = 0
if middle >= 90:
    if final >= 95:
        scholarship = 100000
    elif final >= 90:
        scholarship = 50000
print(scholarship)