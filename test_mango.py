import os
import certifi
import pymongo
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_DB_URL")

if not mongo_url:
    raise ValueError("MONGO_DB_URL is missing from .env")

client = pymongo.MongoClient(
    mongo_url,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

try:
    print(client.admin.command("ping"))
    print("MongoDB connected successfully!")
finally:
    client.close()