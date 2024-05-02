import certifi
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.environ.get("DATABASE_URL")
client = AsyncIOMotorClient(db_url, tlsCAFile=certifi.where())
db = client['ing_software_2']
collection = db['books']
