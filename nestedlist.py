#store data in nested list and access it and print it in tabular form
nested_list=[[1,"Sayiqa",[55,66,77]],[2,"Abdulrehman",[22,77,45]]]
print("Student_ID\tName\tMarks")
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(nested_list[i][j],end="               ")
    print()
#student data entry system
mul_student_list=list()
no_of_students=int(input("Number of students"))
for k in range(no_of_students):
    students_data=list()
    subjects_marks=list()
    id=input(f'Enter the student {k+1} reg.no')
    name=input(f'Enter the student {k+1} name')
    students_data.append(id)
    students_data.append(name)
    no_of_subjects=int(input(f'Enter the number of subjects of student {k+1}'))
    for i in  range(no_of_subjects):
        marks=float(input(f'Enter the student {k+1} subject marks out of 100'))
        subjects_marks.append(marks)
    students_data.append(subjects_marks)
    mul_student_list.append(students_data)
print(mul_student_list)
#access the nested list and print in tabular format
print("Student ID\tStudent Name\tSubject Marks")
for i in range(len(mul_student_list)):
    for j in range(len(mul_student_list[i])):
        print(mul_student_list[i][j],end="          ")
    print()