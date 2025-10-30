from pydantic import BaseModel
from fastapi import FastAPI

class subtractionmodel(BaseModel):
    x: int
    y: int

def subtract(data: subtractionmodel):
    return data.x - data.y

app = FastAPI()

@app.post("/subtractfunc")
def subtract_api(model: subtractionmodel):
    return {"result": subtract(model)}