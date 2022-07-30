student_heights=input("input a list of student heights (separated by space):\n").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
sum_height=0#sum(student_heights)
for i in student_heights:
    sum_height+=i
number_of_student=0#len(student_heights)
for j in student_heights:
    number_of_student+=1
print(f"average:{int(sum_height/number_of_student)}")