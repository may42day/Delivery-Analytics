from motor.motor_asyncio import AsyncIOMotorCollection


async def insert_order_info(collection: AsyncIOMotorCollection, info: OrderInfo):
    await collection.insert_one(info)
    return info
