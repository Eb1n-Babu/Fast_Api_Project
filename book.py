from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI")

book_db = []

class Book(BaseModel):
    title: str
    author: str

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/books")
def get_books():
    return book_db

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return book_db[book_id]

@app.post("/books")
def create_book(book: Book):
    book_db.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    book_db[book_id] = book
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int , book: Book):
    book_db.pop(book_id)
    return book
