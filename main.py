from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

DATA_FILE = 'data/users.json'

class User(BaseModel):
    id: int 
    name: str 
    email: str 

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.get("/users", response_model=List[User])
def get_users():
    users = load_users()
    return users

@app.post("/users", response_model=User)
def create_user(user: User):
    users = load_users()
    users.append(user.dict())
    save_users(users)
    return user
