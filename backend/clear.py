from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
    db = client['avatar_generator']
    generations_collection = db['generations']
    
    result = generations_collection.delete_many({})
    print(f"✓ Successfully cleared {result.deleted_count} jobs from the queue")
    
except Exception as e:
    print(f"✗ Error: {e}")