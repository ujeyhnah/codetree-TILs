def strverse(s):
    s.reverse()
    return ''.join(s)
a = input().split()
x = strverse(a)
a = ''.join(a)
print('Yes' if a == x else 'No' )