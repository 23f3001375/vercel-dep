import csv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_students(request: Request):
    classes = request.query_params.getlist("class")
    results = []

    with open("api/students.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not classes or row["class"] in classes:
                results.append({"studentId": int(row["studentId"]), "class": row["class"]})
    return {"students": results}
