from pymongo import MongoClient
import os
from dotenv import load_dotenv
from redis import Redis

load_dotenv()
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

database = client.zoo_hub_python_api_db


# Defining collection example
# collection_name = database['tickets_collection']
