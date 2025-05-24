from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open(os.path.join(os.path.dirname(__file__), "marks.json")) as f:
    data = json.load(f)

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [next((x["marks"] for x in data if x["name"] == name), None) for name in names]
    return {"marks": marks}
