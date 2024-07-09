room, hallway, toilet = 0, 0, 0
n = int(input())
for i in range(1, n+1):
    if i % 12 == 0:
        toilet += 1
    elif i % 3 == 0:
        hallway += 1
    elif i % 2 == 0:
        room += 1
print(room, hallway, toilet)