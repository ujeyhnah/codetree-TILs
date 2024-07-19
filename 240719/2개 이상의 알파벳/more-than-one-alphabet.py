def func(s):
    result = []
    for i in s:
        if i not in result:
            result.append(i)
    if len(result) >= 2: return True
    else: return False
a = input()
print('Yes' if func(a) else 'No')