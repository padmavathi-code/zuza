from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=60)
    course: str = Field(..., min_length=2, max_length=50)

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

    class Config:
        from_attributes = True