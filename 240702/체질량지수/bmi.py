h, w = map(int, input().split())
bmi = w/pow((h/100),2)

if bmi >= 25:
    print(int(bmi))
    print('Obesity')
else:
    print(int(bmi))