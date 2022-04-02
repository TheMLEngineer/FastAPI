from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return "Hello World"

@app.post('/hello')
def index2():
    return 'Hi'