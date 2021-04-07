from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def sayHi():
    return {"hello", "word"}


@app.get("/item/")
def read_item(id: int):
    return {"itemId": id, "timestamp": time.time()}
