from fastapi import FastAPI
from database import engine, Base
from routers.student_router import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Day 5 Student Management API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Day 5 API Working"}

app.include_router(student_router)