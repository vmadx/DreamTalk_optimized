from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
print(f"Connecting to: {mongo_uri}")

client = MongoClient(mongo_uri)

# List all databases
print("\n=== All Databases ===")
dbs = client.list_database_names()
for db_name in dbs:
    print(f"  - {db_name}")

# Check avatar_generator database
print("\n=== avatar_generator Database ===")
db = client['avatar_generator']
collections = db.list_collection_names()
print(f"Collections: {collections}")

for collection_name in collections:
    collection = db[collection_name]
    count = collection.count_documents({})
    print(f"\n  {collection_name}: {count} documents")
    if count > 0:
        # Show first few documents
        docs = list(collection.find().limit(3))
        for doc in docs:
            print(f"    - {doc}")

# Check if there are other databases with 'avatar' or 'generation' in the name
print("\n=== Checking for other relevant databases ===")
for db_name in dbs:
    if 'avatar' in db_name.lower() or 'generation' in db_name.lower():
        print(f"Found: {db_name}")
        db_check = client[db_name]
        cols = db_check.list_collection_names()
        print(f"  Collections: {cols}")
