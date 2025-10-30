from fastapi import FastAPI
from pydantic import BaseModel

# create an object of FastAPI class
app = FastAPI()

user_db = {
    1: {"name": "Ray", "age": 33},
    2: {"name": "Alice", "age": 28},
    3: {"name": "Bob", "age": 25}
}
 
#lets update the above records with th e help of put method

class User(BaseModel):
    name: str
    age: int

@app.put("/user_db/v1/update/{user_id}")
def user_update(user_id:int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}
    
    
#now lets see with delete method

@app.delete("/user_db/v1/delete/{user_id}")

def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}