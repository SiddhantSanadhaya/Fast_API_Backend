from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True #default, will work if default assigned, can be None

@app.get('/')
def get_users():
    user_list = [1,2,3,4,5]
    return {"response":user_list}

@app.get('/posts')
def get_posts():
    post_list = [1,2,3,4,5]
    return {"response":post_list}

@app.post('/')
def post(payload:Post):
    print(payload)
    return {"message":"Successfully created post"}
