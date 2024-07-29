class Student:
    def __init__(self, cm, kg, idx):
        self.cm = cm
        self.kg = kg
        self.idx = idx
students = []
for i in range(int(input())):
    cm, kg = map(int, input().split())
    students.append(Student(cm, kg, i+1))
students.sort(key=lambda x: (x.cm, -x.kg))
for st in students:
    print(st.cm, st.kg, st.idx)