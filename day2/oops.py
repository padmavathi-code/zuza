class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student(101, "Padma", "Python")
student2 = Student(102, "Priya", "Java")

student1.display_student()

print("----------------")

student2.display_student()