from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author: str
    isbn: str
