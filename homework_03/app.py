from fastapi import FastAPI


app = FastAPI() # You should consider

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/ping")
def read_root():
    return {"message": "pong"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


