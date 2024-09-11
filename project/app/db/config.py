import beanie
import motor
# import os
import motor.motor_asyncio

from app.db.models import community, dwelling, subscription
from app.db.models import admin_user, app_user, community_user


async def init_db(db_uri: str, db_name: str):

    client = motor.motor_asyncio.AsyncIOMotorClient(
        db_uri,
        uuidRepresentation="standard",
    )

    await beanie.init_beanie(
        database=client[db_name],
        document_models=[
            admin_user.admin_user_model,
            app_user.app_users_model,
            community_user.community_users_model,
            community.community_model,
            dwelling.dwelling_model,
            subscription.subscription_model

        ],
    )
