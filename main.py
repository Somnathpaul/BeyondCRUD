from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/{username}')
async def first_route(username: str):
    return {"message": f"Hello {username}"}


l1 = ['husky', 'crow']
@app.get('/search/{username}')
async def search_name(username:str):

    for name in l1:
        if username in l1:
            return {f"name found: {username}"}
        else:
            return {"name not found"}
        

@app.get('/greet/')
async def greet_name(username: Optional[str] = "none"):
    return {"hello": f"{username}"}
    

from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    age: int


@app.post('/account')
async def account(user_data:UserSchema, id: Optional[int] = 1):
    new_user ={
        "name" : user_data.name,
        "age" : user_data.age,
        "id" : id
    }

    return {f"new users created {new_user}"}