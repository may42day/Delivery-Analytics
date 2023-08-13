from enum import Enum
from typing import List
from fastapi import APIRouter, Depends

from models.queue_models import QueueSatusType
from utils.date_models import DaysPeriodParam, YearMonthPeriodParam, YearPeriodParam

router = APIRouter()


@router.get("/count/day/{date}")
async def count_queue_per_day(date: str, status: QueueSatusType = None):
    return {"date": date, "status": status}


@router.get("/count/days")
async def count_queue_per_days_period(
    days_period: DaysPeriodParam = Depends(), status: QueueSatusType = None
):
    return {"start_date": 1, "end_date": 2, "status": status}


@router.get("/count/month/{year}/{month}")
async def count_queue_per_month(year: int, month: int, status: QueueSatusType = None):
    return {"year": year, "month": month, "status": status}


@router.get("/count/months/")
async def count_queue_per_months_period(
    year_month_period: YearMonthPeriodParam = Depends(),
    status: QueueSatusType = None,
):
    return {
        "start_year": 1,
        "start_month": 2,
        "end_year": 3,
        "end_month": 4,
        "status": status,
    }


@router.get("/count/year/{year}")
async def count_queue_per_year(year: int, status: QueueSatusType = None):
    return {"year": year, "month": 1, "status": status}


@router.get("/count/years/")
async def count_queue_per_year_period(
    year_period: YearPeriodParam = Depends(),
    status: QueueSatusType = None,
):
    return {
        "start_year": 1,
        "end_year": 2,
        "status": status,
    }


@router.get("/average-time/day/{date}")
async def get_average_queue_time_per_day(date: str):
    return {"date": date, "status": 1}


@router.get("/average-time/days")
async def get_average_queue_time_per_days_period(
    days_period: DaysPeriodParam = Depends(),
):
    return {"start_date": 2, "end_date": 1, "status": 1}


@router.get("/average-time/month/{year}/{month}")
async def get_average_queue_time_per_month(year: int, month: int):
    return {"year": year, "month": month, "status": 1}


@router.get("/average-time/months/")
async def get_average_queue_time_per_months_period(
    year_month_period: YearMonthPeriodParam = Depends(),
):
    return {
        "start_year": 1,
        "start_month": 2,
        "end_year": 3,
        "end_month": 4,
        "status": 1,
    }


@router.get("/average-time/year/{year}")
async def get_average_queue_time_per_year(year: int):
    return {"year": year, "status": 1}


@router.get("/average-time/years/")
async def get_average_queue_time_per_year_period(
    year_period: YearPeriodParam = Depends(),
):
    return {
        "start_year": 1,
        "end_year": 2,
        "status": 1,
    }
