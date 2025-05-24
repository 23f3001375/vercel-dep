from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students_data = []

with open("students.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students_data.append(row)

@app.get("/api")
def get_students(class_filter: list[str] | None = Query(None, alias="class")):
    if class_filter:
        filtered_students = [
            student for student in students_data if student["class"] in class_filter
        ]
        return JSONResponse(content={"students": filtered_students})
    return JSONResponse(content={"students": students_data})

# To run this, save it as a Python file (e.g., main.py)
# and then run using uvicorn: uvicorn main:app --reload

# The API endpoint URL will be http://127.0.0.1:8000/api