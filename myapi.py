from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

students = [
    Student(name="areen", age=22, year="year 4"),
    Student(name="hsuam", age=29, year="year 0"),
]

@app.get("/")
def index():
    return {"message": "First Data"}

@app.get("/get-students/{index}")
def get_student(index: int = Path(..., description="Index of student", ge=0)):
    if index >= len(students):
        return {"Error": "Student not found"}
    return students[index]

@app.get("/get-by-name/")
def get_student_by_name(name: Optional[str] = None):
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return {"Data": "Not found"}

@app.post("/create-student/")
def create_student(student: Student):
    students.append(student)
    return {"Message": "Student added", "student": student}

@app.put("/update-student/{index}")
def update_student(index: int, student: UpdateStudent):
    if index >= len(students):
        return {"Error": "Student does not exist"}

    existing = students[index]

    updated = Student(
        name=student.name if student.name is not None else existing.name,
        age=student.age if student.age is not None else existing.age,
        year=student.year if student.year is not None else existing.year
    )

    students[index] = updated
    return {"Message": "Student updated", "student": updated}


@app.delete("/delete-student/{index}")
def delete_student(index: int = Path(..., description="Index of student", ge=0)):
    if index >= len(students):
        return {"Error": "Student does not exist"}
    
    removed_student = students.pop(index)
    return {
        "Message": "Student deleted successfully",
        "Deleted Student": removed_student
    }
