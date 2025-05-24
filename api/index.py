from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

CSV_PATH = os.path.join(os.path.dirname(__file__), 'students.csv')

students = []
with open(CSV_PATH, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert studentId to int
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
def get_students(request: Request):
    classes = request.query_params.getlist("class")  # get all class filters
    
    if classes:
        # Filter students by class but keep original order
        filtered_students = [s for s in students if s["class"] in classes]
    else:
        filtered_students = students
    
    return {"students": filtered_students}
