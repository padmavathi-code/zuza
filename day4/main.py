from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


import models
from database import engine, SessionLocal

from schemas import StudentCreate, StudentResponse


models.Base.metadata.create_all(
    bind=engine
)


app = FastAPI()



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.get("/")
def home():

    return {
        "message":"Day 4 FastAPI MySQL CRUD API"
    }



# CREATE STUDENT

@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = models.Student(
        name=student.name,
        age=student.age,
        course=student.course
    )


    db.add(new_student)

    db.commit()

    db.refresh(new_student)


    return new_student



# READ STUDENTS

@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(
        models.Student
    ).all()


    return students



# DELETE STUDENT

@app.delete("/students/{id}")
def delete_student(
    id:int,
    db:Session=Depends(get_db)
):

    student = db.query(
        models.Student
    ).filter(
        models.Student.id==id
    ).first()


    if student:

        db.delete(student)

        db.commit()


        return {
            "message":"Student deleted"
        }


    return {
        "message":"Student not found"
    }