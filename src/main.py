import uuid

from fastapi import FastAPI

from repositories.surf_classes_repository import SurfClassesRepository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hola")
async def aaa():
    return SurfClassesRepository().find_all()

@app.get("/holass")
async def aaass():
    return SurfClassesRepository().find_by_id(uuid.uuid4())
