from fastapi import Body, FastAPI

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

@app.get("/books/")
async def get_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def get_book_by_author_and_category(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
        book.get("category").casefold() == category.casefold():
            books_to_return.append(book)       
    return books_to_return

@app.post("/books/create_book")
async def add_book(new_book = Body()):
    BOOKS.append(new_book)
