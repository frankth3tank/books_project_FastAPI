# Books Project FastAPI
This repository contains the code for a Books project API built with FastAPI. This API allows users to perform CRUD operations (Create, Read, Update, Delete) on books data.

## Prerequisites
To run this project, you need to have Python 3.7 or later installed on your machine. You also need to have pip installed.

## Installation
1. Clone this repository to your local machine.
```
git clone https://github.com/frankth3tank/books_project_FastAPI.git
```
2. Change into the project directory.
```
cd books_project_FastAPI
```
3. Create a virtual environment and activate it.
```
python -m venv env
source env/bin/activate
```
4. Install the dependencies.
```
pip install -r requirements.txt
```

## Usage
1. Start the API server.
```
uvicorn books:app --reload
```
2. Navigate to http://localhost:8000/docs in your web browser to access the Swagger UI. Here, you can test the different endpoints available in the API.

## Endpoints
- `GET /books` Returns a list of all books.
- `GET /books/{book_title}` Returns the details of a single book by providing the title.
- `GET /books/?category` Returns a list of all books that match a specific category.
- `GET /books/byauthor/?author` Returns a list of all books that match a specific author.
- `GET /books/{book_author}/?category` Returns a list of all books that match a specific author and category.
- `POST /books/create_book` Creates a new book.
- `PUT /books/update_book` Updates the details of a book that matches the title.
- `DELETE /books/delete_book/{book_title}` Deletes a book that matches the title.

## Contributing
If you would like to contribute to this project, please open a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License
This project is licensed under the MIT License.