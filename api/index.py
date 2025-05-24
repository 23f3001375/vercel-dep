from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students = []

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Make sure studentId is int and class is exact string from CSV
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
def get_students(request: Request):
    classes = request.query_params.getlist("class")
    if classes:
        filtered = [s for s in students if s["class"] in classes]
    else:
        filtered = students
    return {"students": filtered}
