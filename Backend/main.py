# -*- coding: utf-8 -*-00
"""
@author: FaizanMunsaf

Basic Application using FastApi

Backend Server using is uvicorn for local host

so we can use sweggare also 

localhot:8000/docs

for infrastructure

localhot:8000/redoc

for run the server use this

uvicorn main:app --reload
"""
from typing import List
from fastapi import FastAPI, HTTPException
import uvicorn
from uuid import uuid4, UUID
from model import User, Gender, Role, UserUpdateRequest


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("07862256-4b63-43d6-b1d1-2f2c7fe6b1d3"),
        first_name="Ghania",
        last_name="Iftikhar",
        gender=Gender.female,
        roles=[Role.student]
    ),

    User(
        id=UUID("05df4b89-6c31-46f2-9a49-ca52cf13a2ef"),
        first_name="Faizan",
        last_name="Munsaf",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return True

    raise HTTPException(
        status_code=404,
        detail=f"user wid id: {user_id} doesn't exists"
    )


@app.put("/api/v1/users{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles

            return True

    raise HTTPException(
        status_code=404,
        detail=f"user wid id: {user_id} doesn't exists"
    )

# Main Function for server
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
