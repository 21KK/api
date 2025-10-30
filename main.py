from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str
    
@app.post("/register")
def register_user(user: User):
    return {"message":f"User '{user.username}' registered successfully"}
