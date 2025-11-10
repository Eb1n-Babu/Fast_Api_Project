from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")

db_book = []

class book(BaseModel):
    author: str
    title: str

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/books")
def books():
    return db_book

@app.get("/books/{book_id}")
def book(book_id: int):
    return db_book[book_id]

@app.post("/books/")
def create_book(book: book):
    db_book.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: book):
    db_book[book_id] = book
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db_book.pop(book_id)
    return book


