from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")

book_data_base = []

class Book(BaseModel):
    title: str
    author: str

@app.get("/books")
def get_books():
    return book_data_base

@app.post("/books")
def create_book(book: Book):
    book_data_base.append(book)

@app.get("/books/{book_id}")
def get_book(book_id: int):
    try:
        global book_data_base
        return book_data_base[book_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    try:
        global book_data_base
        book_data_base[book_id] = book
        return book_data_base[book_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        book_data_base.pop(book_id)
        return book_data_base
    except IndexError:
        raise HTTPException(status_code=404, detail="Book not found")