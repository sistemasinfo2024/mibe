from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def saludo():
    return {'saludo': "Welcome to mibe"}
