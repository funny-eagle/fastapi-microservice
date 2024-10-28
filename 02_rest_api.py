from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

valid_users = dict()


class User(BaseModel):
    username: str
    password: str


@app.post("/login/signup")
def signup(uname: str, passwd: str):
    if uname is None and passwd is None:
        return {"message": "invalid user"}
    elif not valid_users.get(uname) is None:
        return {"message": "user exists"}
    else:
        user = User(username=uname, password=passwd)
        valid_users[uname] = user
        return user


@app.get("/login")
def login(username: str, password: str):
    if valid_users.get(username) is None:
        return {"message": "user does not exists"}
    else:
        user = valid_users.get(username)
        if password == user.password:
            return user
        else:
            return {"message": "user or password do not match"}


@app.delete("/login/remove/{username}")
def delete_user(username: str):
    if username is None:
        return {"message": "invalid user"}
    else:
        del valid_users[username]
        return {"message": "deleted user"}
