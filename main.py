from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from database.core import Base, engine
from note.views import router as note_router


def custom_generate_unique_id(route: APIRoute):
    # needed for better client code generation method names
    return f"{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

app.include_router(note_router, prefix="/notes", tags=["notes"])

Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
