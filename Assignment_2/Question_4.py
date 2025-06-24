#Question_1
name = input("Enter student name: ")
student_class = input("Enter student class: ")

marks = []
for i in range(1, 6):
    mark = float(input("Enter marks for subjects: "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'


print("\nStudent Details\n")
print("Name",name)
print("Class",student_class)
print("Total Marks",total)
print("Percentage",percentage)
print("Grade",grade)