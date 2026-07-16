from models.student_model import Student


# CREATE STUDENT
def create_student(db, student):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student



# GET ALL STUDENTS
def get_students(db):

    return db.query(Student).all()



# GET STUDENT BY ID  ✅ ADD THIS
def get_student_by_id(db, student_id):

    return db.query(Student).filter(
        Student.id == student_id
    ).first()



# UPDATE STUDENT  ✅ ADD THIS
def update_student(db, student_id, student):

    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if existing_student is None:
        return None


    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.course = student.course


    db.commit()
    db.refresh(existing_student)

    return existing_student



# DELETE STUDENT
def delete_student(db, student_id):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if student:

        db.delete(student)
        db.commit()

        return True


    return False