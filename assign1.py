from fastapi import FastAPI
from pydantic import BaseModel

class multiplymodel(BaseModel):
    a:int
    b:int
    
def multiply(data: multiplymodel):
   return data.a *data.b

app = FastAPI()
@app.post("/multiply")

def multiply_api(model: multiplymodel):
    return multiply(model)

import requests

payload = {
    "a": 5,
    "b": 6
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post("http://localhost:8000/multiply", json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.json())

