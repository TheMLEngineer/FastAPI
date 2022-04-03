from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/hello')
def index():
    return {"message" : "Hello World!"}

# Commenting this fn to define more advanced get_all_blogs fn
#@app.get('/blog/all')
#def get_all_blogs():
#    return {'message' : 'All blogs provided'}

@app.get('/blog/all')
def get_all_blogs(page , page_size):
    return {'message' : f'All {page_size} blogs on page {page}'}








class BlogType(str , Enum):
    # Defining blog types
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type : BlogType):
    return {'message' : f'Blog type {type}'}



@app.get('/blog/{id}')
def get_blog(id : int) :
    return {'message' : f'Blog with id {id}'}


