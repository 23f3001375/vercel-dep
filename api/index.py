from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from CSV
df = pd.read_csv("marks.csv")

@app.get("/")
async def get_marks(name: list[str] = []):
    results = []
    for n in name:
        match = df[df['name'].str.lower() == n.lower()]
        if not match.empty:
            results.append(int(match['marks'].values[0]))
        else:
            results.append(None)
    return JSONResponse(content={"marks": results})
