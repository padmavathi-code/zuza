from fastapi import FastAPI

app=FastAPI(title="Student Management")
@app.get("/")
def home():
    return{"this is home page"}