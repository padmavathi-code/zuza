class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display_student(self):
        self.display_name()
        print("Course:", self.course)


student = Student("Padma", "Python")

student.display_student()