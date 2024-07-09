dic = {1:'John', 2:'Tom', 3:'Paul', 4:'Sam'}
while(True):
    x = int(input())
    try:
        print(dic[x])
    except:
        print('Vacancy')
        break