from fastapi import FastAPI, HTTPException
from db.db import client
from controller.bookCRUD import router as book_router

app = FastAPI()
app.include_router(book_router, tags=["books"], prefix="/books")
# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()
