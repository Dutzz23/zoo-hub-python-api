from pymongo import MongoClient

uri = "mongodb+srv://Dutzz:mTducQ22TviowDpx@cluster0.e0wvocd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

database = client.zoo_hub_python_api_db

# Defining collection example
# collection_name = database['tickets_collection']