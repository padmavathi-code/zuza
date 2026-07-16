from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.student_schema import StudentCreate, StudentResponse

from services.student_service import (
    create_student,
    get_students,
    delete_student,
    get_student_by_id,
    update_student
)

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@router.get("/")
def view_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    deleted = delete_student(db, student_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}


@router.get("/{student_id}", response_model=StudentResponse)
def view_student(student_id: int, db: Session = Depends(get_db)):

    student = get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student




@router.put("/{student_id}", response_model=StudentResponse)
def edit_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    updated_student = update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return updated_student