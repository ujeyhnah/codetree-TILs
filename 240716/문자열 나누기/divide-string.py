n = int(input())
result = input().replace(' ', '')
for i in range(len(result)):
    if i!=0 and i % 5 == 0:
        print()
        print(result[i],end='')
    else:
        print(result[i],end='')