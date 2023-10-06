from student import Student
from faculty import Faculty

st1 = Student("John", "Doe", "john.doe@gmail.com", "1991-01-01", False, "1990-01-01")   
st2 = Student("Jane", "Doe", "jane.doe@gmail.com", False, "1991-01-01")
st3 = Student("John", "Smith", "john.smith@gmail.com", False, "1992-01-01")
st4 = Student("Jane", "Smith", "jane.smith@gmail.com", False, "1993-01-01")

f1 = Faculty("Faculty of Computer Science", "FCS", "Computer Science")
print(f1.name)
print(f1.abbreviation)
print(f1.students)
print(f1.study_field)
print(f1.graduate_students)

f1.enroll_student(st1)
f1.enroll_student(st2)
f1.enroll_student(st3)
f1.enroll_student(st4)

print(f"Check student before graduation {f1.has_student(st1)}")
print(f"Check student before graduation {f1.has_student(st2)}")

f1.graduate_student(st1)

print(f"Check student after graduation {f1.has_student(st1)}")

print(f1)
print(st1)