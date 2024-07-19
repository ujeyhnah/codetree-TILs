def strverse(s):
    result = list(s.split())
    result.reverse()
    return ''.join(result)
a = input()
x = strverse(a)
print('Yes' if a == x else 'No' )