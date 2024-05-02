from typing import List

from fastapi import HTTPException, APIRouter
from db.db import collection
from model.book import Book

router = APIRouter()

@router.post("/", response_description="Create new book", response_model=Book)
async def create_book(b: Book):
    existing_book = await collection.find_one({"isbn": b.isbn})

    if existing_book != None :
        raise HTTPException(status_code=400, detail="Bad Request: Book already exists")

    result = collection.insert_one(b.dict())

    return b

@router.get("/", response_description="List books", response_model=List[Book])
async def read_all_books():
    books = await collection.find().to_list(100)

    for book in books:
        book["_id"] = str(book["_id"])

    return books

@router.get("/{isbn}", response_model=Book)
async def read_book_by_isbn(isbn: str):
    book = await collection.find_one({"isbn": isbn})

    if book:
        return book

    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{isbn}", response_model=Book)
async def update_book(isbn: str, b: Book):
    updated_book = await collection.find_one_and_update(
        {"isbn": isbn}, {"$set": b.dict()}
    )

    if updated_book:
        return b

    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{isbn}", response_model=Book)
async def delete_book(isbn: str):
    deleted_book = await collection.find_one_and_delete({"isbn": isbn})

    if deleted_book:
        return deleted_book

    raise HTTPException(status_code=404, detail="Book not found")
