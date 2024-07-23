class Info:
    def __init__(self, _id='codetree', level='10'):
        self._id = _id
        self.level = level

_id, lev = input().split()
x1 = Info()
x2 = Info(_id, lev)
print(f'user {x1._id} lv {x1.level}')
print(f'user {x2._id} lv {x2.level}')