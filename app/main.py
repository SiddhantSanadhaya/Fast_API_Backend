from fastapi import FastAPI, Depends, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

import psycopg2
import models
from sqlalchemy.orm import Session
from database import engine, get_db
models.Base.metadata.create_all(bind=engine)
app = FastAPI()



class Post(BaseModel):
    title:str
    content:str
    published: bool = True #default, will work if default assigned, can be None

posts = {}


@app.get('/')
def get_users():
    user_list = [1,2,3,4,5]
    return {"response":user_list}

@app.get('/posts')
def get_posts():

    return {"response":posts}

@app.get('/posts/{id}')
def get_posts(id:int, response:Response):
    if id not in posts:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = f"Post not found"
            )
   
        return {"response": "Post not found"}

    return {"response":posts[id]}

@app.post('/',status_code = status.HTTP_201_CREATED)
def create_posts(payload:Post,db: Session = Depends(get_db)):

    if not posts:
        posts[1] = payload.dict()
    else:
        posts[list(posts.keys())[-1]+1] = payload.dict()


    return {"message":"Successfully created post"}

@app.delete('/posts/{id}')
def delete_post(id:int):
    if id in posts:
        posts.pop(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = f"Post not found"
            )


            
@app.put('/{id}',status_code = status.HTTP_201_CREATED)
def update_posts(payload:Post,id:int):
    if id in posts:
        posts[id] = payload
        return {"response": "Successfully Updated"}
    
    raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = f"Post not found"
            )

