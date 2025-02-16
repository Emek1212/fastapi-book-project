from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Stage 1"}

@app.get("/stage2")
def stage2():
    return {"message": "Welcome to Stage 2"}

