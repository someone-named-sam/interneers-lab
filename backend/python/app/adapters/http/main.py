from fastapi import FastAPI, Query
from app.domain.service import greet_user

app = FastAPI(title="Hexagonal GET API")

@app.get("/greet")
def greet(name: str = Query(..., description="Your name"),
          age: int = Query(..., description="Your age")):
    message = greet_user(name, age)
    return {"message": message}