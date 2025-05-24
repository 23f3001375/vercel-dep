from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

with open("students.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)

@app.get("/students")
def get_students(class_filter: str | None = Query(None, alias="class")):
    if class_filter:
        filtered = [s for s in students if s["class"] == class_filter]
        return JSONResponse(content=filtered)
    return JSONResponse(content=students)
