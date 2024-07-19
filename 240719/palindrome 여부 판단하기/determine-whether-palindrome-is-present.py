def strverse(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result
a = input()
x = strverse(a)
print('Yes' if a == x else 'No' )