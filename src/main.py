from fastapi import FastAPI

from repositories.product_repository import ProductRepository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hola")
async def aaa():
    return ProductRepository().find_all()
