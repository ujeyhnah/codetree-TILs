n = int(input())
arr = list(map(float, input().split()))
score = sum(arr)/len(arr)
print(f'{score:.1f}')
if score >= 4.0:
    print('Perfect')
elif score >= 3.0:
    print('Good')
else:
    print('Poor')