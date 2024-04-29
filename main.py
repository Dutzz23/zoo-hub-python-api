from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from animals_monitor.router_animals_monitor import animals_monitor_router
from employees_chat.router_employees_chat import employees_chat_router

app = FastAPI()
app.include_router(animals_monitor_router)
app.include_router(employees_chat_router)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# lab2, lab3, prezentari, lab4 cod sursa, materiale utile, exemple probleme sockets, test1, test2

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Dutzz:mTducQ22TviowDpx@cluster0.e0wvocd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged!")

except Exception as e:
    print(e)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
