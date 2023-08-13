from config import DATABASE_URL

import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
database = client.AnalyticService


async def get_registrations_collection():
    return database.registrations
