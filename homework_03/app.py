# lesson 13 part 1 15:10
from fastapi import FastAPI
# from pythonping import ping

app = FastAPI()


# строка запуска
# (venv) user@user-desktop:~/pythonProject/OTUSPython/homework_03$ uvicorn app:app --reload
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/ping")
def read_root():
    return {"message": "pong"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# pong_waiter = await ws.ping()
# await pong_waiter
# # Я ничего не получил. После этого я также выполняю:
#
# pong_waiter.result()