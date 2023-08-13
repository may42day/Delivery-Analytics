from datetime import datetime, timedelta
import enum
from typing import List
from models.user_models import RegCounter, RegistrationInfo, Roles
from utils.date_models import PeriodFormats
from motor.motor_asyncio import AsyncIOMotorCollection


async def insert_reg_info(collection: AsyncIOMotorCollection, info: RegistrationInfo):
    await collection.insert_one(info)
    return info


async def get_reg_amount_for_specific_date(
    collection: AsyncIOMotorCollection,
    start_date: datetime,
    end_date: datetime,
    role: Roles,
) -> int:
    query = {"created_at": {"$gte": start_date, "$lt": end_date}}
    if role:
        query["role"] = role.value
    count = await collection.count_documents(query)
    return count


async def get_reg_amount_for_period(
    collection: AsyncIOMotorCollection,
    start_date: datetime,
    end_date: datetime,
    role: Roles,
    period_format: PeriodFormats,
) -> List[RegCounter]:
    query = [
        {"$match": {"created_at": {"$gte": start_date, "$lte": end_date}}},
        {
            "$project": {
                "date": {
                    "$dateToString": {
                        "format": period_format.value,
                        "date": "$created_at",
                    }
                }
            }
        },
        {"$group": {"_id": "$date", "amount": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
    ]
    if role:
        query[0]["$match"]["role"] = {"$eq": role.value}

    aggregation = collection.aggregate(query)
    counters = []
    async for document in aggregation:
        counters.append(RegCounter(date=document["_id"], amount=document["amount"]))
    return counters
