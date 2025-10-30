# To Create api, you have lot of methods, get, post, put, delete etc.
# Can use FastAPI to create api
# Install a frameweork using pip
# Install uvicorn to run the api server: makes api avaialable to the world

from fastapi import FastAPI

# Create a fucntion of FastAPI class
def add(a, b):
    return a + b

# Call the function 
add(2, 3)

# You cannot see the output because it is not printed
print(add(2, 3))

# To expose this function to the outside world in any form of api like REST API, url, google cloud function, lambda function etc.
# This can be done using API with FastAPI
# We will use fastapi to create an api
# Create an object(Variable) of FastAPI class

app = FastAPI()
@app.get("/ray/21")  # Decorator to define the root endpoint, only this much is required to create an api
def add(x:int,y:int):
    return x + y

#decorator is used to define the endpoint of the api
# here /ray/21 is the endpoint of the api

#To run the api server, use the command in terminal: can use Uvicorn
# uvicorn createAPI:app --reload

# define the data type at each parameter
# x:int means x is of type integer, it is because you can define the data type of each parameter independently
# Also you can custome define the root endpoint
# @app.get("/add")  # Decorator to define the root endpoint


#Another meaning of "Get" is to retrieve data from the server
#technical meaning, we are trying to send the data which will be exposed to the outside world

#lets do another api for subtraction
#lets convert the entire code into a post method


#the main difference between get and post is that get is used to retrieve data from the server, 
# post is used to send data to the server, that means you cannot access the post api directly from the browser
# you need to use some tool like postman or any other tool to access the post api 
# Simple ,eaning, post method is just posting the data to the server, not retrieving it
# In real world, get method is used to retrieve data from the server

#if the data is not being verifioed in the postman, it may be because the data type is not matching or
#something called as pydantic validation error
#pydantic is a library used by fastapi to validate the data type of the parameters
#Pydantic is set of rules to validate the data type of the parameters
# Because post is secure method, it is important to validate the data type of the parameters using pydantic

from pydantic import BaseModel

class subtractModel(BaseModel):
    x: int
    y: int

def subtract(x:int,y:int):
    return x - y

@app.post("/subtract2")
def subtract_number(model: subtractModel):
    return subtract(model.x, model.y)
                    