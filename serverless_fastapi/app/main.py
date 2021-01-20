from fastapi import FastAPI
from mangum import Mangum
import os

prefix = '/' + os.environ.get('ENV', "").lower()

app = FastAPI(title="Demonstração do FastAPI no Lambda", openapi_prefix=prefix)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


handler = Mangum(app)
