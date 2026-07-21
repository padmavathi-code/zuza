from fastapi import FastAPI

app = FastAPI(
    title="Student Management System"
)


@app.get("/")
def home():
    return {
        "message": "Student Management Backend Running"
    }