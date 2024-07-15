n = int(input())
count_arr = [0] * 9
arr = list(map(int, input().split()))
for i in arr:
    count_arr[i-1] += 1
for i in count_arr:
    print(i)