import beanie
import motor
import os
import motor.motor_asyncio

from app.db.models import community


async def init_db(db_name=None):
    db_name = db_name or os.getenv("AQUESA_DB_NAME")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        os.getenv("AQUESA_DB"),
        uuidRepresentation="standard"
    )

    await beanie.init_beanie(
        database=client[db_name],
        document_models=[
            community.community_model,
        ],
    )
