from fastapi import FastAPI, HTTPException
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
    try:
        return book_db[book_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def create_book(book: Book):
    book_db.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    try:
        book_db[book_id] = book
        return book
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int , book: Book):
    try:
        book_db.pop(book_id)
        return book
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")
