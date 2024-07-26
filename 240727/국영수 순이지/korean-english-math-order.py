class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for _ in range(n):
    x = input().split()
    students.append(Score(x[0], int(x[1]), int(x[2]), int(x[3])))

students.sort(key = lambda x:(-x.kor, -x.eng, -x.math))
for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math)