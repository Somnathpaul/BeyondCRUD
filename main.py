from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()
'''
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
'''  

from pydantic import BaseModel

'''
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

'''

class BookSchema(BaseModel):
    id: int
    name: str
    author: str
    year: int
    price: int
    account_type: Optional[str] = "User"



books = []

# create book
@app.post('/book')
async def create_book(book_data: BookSchema):
    new_book={
        "id" : book_data.id,
        "name": book_data.name,
        "author": book_data.author,
        "year": book_data.year,
        "price": book_data.price,
        "account_type": book_data.account_type
    }

    books.append(new_book)
    return {f"new book created: {new_book}"}

# get book by id
@app.get('/book')
async def get_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return {"204": "book found"}
        else:
            return {"error"}


# get all books

@app.get("/books")
async def get_all_books():
    return books





# delete a book



