class Student:
    def __init__(self, cm, kg, idx):
        self.cm = cm
        self.kg = kg
        self.idx = idx

n = int(input())
students = []
for i in range(n):
    x = input().split()
    students.append(Student(int(x[0]),int(x[1]), i+1))

students.sort(key=lambda x: (-x.cm, -x.kg, i))
for st in students:
    print(st.cm, st.kg, st.idx)