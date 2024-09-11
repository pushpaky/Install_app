from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

# from app.auth.config import firebase_init
from app.db import config
# from app.routers import api
from app.config import get_settings, Settings

app = FastAPI()


@asynccontextmanager
async def get_db(app: FastAPI):

    # Connect to Firebase...
    # await firebase_init()

    # Get DB Secrets...
    settings = get_settings()
    db_uri = settings.db_uri
    db_name = settings.db_name

    # Connect to Database...
    await config.init_db(db_uri, db_name)
    print("Connected to database")
    yield

app = FastAPI(
    title="Aquesa Launch App Apis",
    summary="Provides APIs for Managing Users and Aquesa Customers",
    description="Launch App APIs for Aquesa",
    version="1.0.0",
    lifespan=get_db,
)

# app.include_router(
#     api.router,
#     prefix="/api",
# )


@app.get("/", tags=["Server Health"])
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Aquesa Launch App APIs",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@app.get("/health", tags=["Server Health"])
async def health():
    return {"ping": True}
