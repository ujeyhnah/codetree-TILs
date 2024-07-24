class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    students.append(Student(name, score))

min_val = students[0].score
k = 0
for i in range(1, 5):
    if min_val > students[i].score:
        min_val = students[i].score
        k = i
print(students[k].name, students[k].score)