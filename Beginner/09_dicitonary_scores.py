student_score={
"Harry": 81,
"Ron":78,
"Hermione":99,
"Draco":74,
"Neville":62
}
student_grade={}
for i in student_score:
    if student_score[i] >90:
        student_grade[i]="Outstanding"
    elif student_score[i] >80:
        student_grade[i]="Exceeds Expectations"
    elif student_score[i] >70:
        student_grade[i]="Acceptable"
    else:
        student_grade[i]="Fail"

print(student_grade)