from pymongo import MongoClient

uri = "mongodb+srv://Dutzz:mTducQ22TviowDpx@cluster0.e0wvocd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.zoo_hub_db

collection_name = db['tickets_collection']