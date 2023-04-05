from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
