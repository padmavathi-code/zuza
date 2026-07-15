from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Welcome API
@app.get("/")
def welcome():
    return {
        "message": "Welcome to Day 3 FastAPI"
    }


# Student Model
class Student(BaseModel):
    name: str
    age: int
    course: str


students = []


# Create Student API
@app.post("/students")
def create_student(student: Student):

    data = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(data)

    return {
        "message": "Student added",
        "data": data
    }


# Get Students API
@app.get("/students")
def get_students():

    return students


# Path Parameter
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Calculator API
@app.get("/calculator")
def calculator(
    num1: float,
    num2: float,
    operation: str
):

    if operation == "add":
        result = num1 + num2

    elif operation == "sub":
        result = num1 - num2

    elif operation == "mul":
        result = num1 * num2

    elif operation == "div":

        if num2 == 0:
            return {
                "error": "Cannot divide by zero"
            }

        result = num1 / num2

    else:
        return {
            "error": "Invalid operation"
        }

    return {
        "result": result
    }


# Product API

class Product(BaseModel):
    name: str
    price: float


products = []


@app.post("/products")
def create_product(product: Product):

    products.append(product)

    return {
        "message": "Product created",
        "product": product
    }


@app.get("/products")
def get_products():

    return products