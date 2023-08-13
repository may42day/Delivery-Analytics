from typing import List
from fastapi import APIRouter
from fastapi import Depends
from repository.user_repository import (
    get_reg_amount_for_period,
    get_reg_amount_for_specific_date,
)
from resources.mongodb import get_registrations_collection
from utils.date_models import (
    DaysPeriodParam,
    DayParam,
    PeriodFormats,
    YearMonthParam,
    YearMonthPeriodParam,
    YearParam,
    YearPeriodParam,
)
from models.user_models import RegCounter, Roles

router = APIRouter()


@router.get("/day/{day}")
async def count_registrations_per_day(day: str, role: Roles = None) -> RegCounter:
    day = DayParam(start_day=day)
    collection = await get_registrations_collection()
    start_date, end_date = day.date_borders()
    amount = await get_reg_amount_for_specific_date(
        collection, start_date, end_date, role
    )
    response = RegCounter(date=day.start_day, amount=amount)
    return response


@router.get("/days")
async def count_registrations_per_days_period(
    days_period: DaysPeriodParam = Depends(), role: Roles = None
) -> List[RegCounter]:
    start_date, end_date = days_period.date_borders()
    collection = await get_registrations_collection()
    reg_counter = await get_reg_amount_for_period(
        collection, start_date, end_date, role, PeriodFormats.days
    )
    return reg_counter


@router.get("/month/{year}/{month}")
async def count_registrations_per_month(
    year: int, month: int, role: Roles = None
) -> RegCounter:
    year_month = YearMonthParam(start_year=year, start_month=month)
    collection = await get_registrations_collection()
    start_date, end_date = year_month.date_borders()
    amount = await get_reg_amount_for_specific_date(
        collection, start_date, end_date, role
    )
    response = RegCounter(date="{year}-{month}", amount=amount)
    return response


@router.get("/months")
async def count_registrations_per_months_period(
    year_month_period: YearMonthPeriodParam = Depends(), role: Roles = None
) -> List[RegCounter]:
    collection = await get_registrations_collection()
    start_date, end_date = year_month_period.date_borders()
    reg_counter = await get_reg_amount_for_period(
        collection, start_date, end_date, role, PeriodFormats.months
    )
    return reg_counter


@router.get("/year/{year}")
async def count_registrations_per_year(year: int, role: Roles = None) -> RegCounter:
    year = YearParam(start_year=year)
    collection = await get_registrations_collection()
    start_date, end_date = year.date_borders()
    amount = await get_reg_amount_for_specific_date(
        collection, start_date, end_date, role
    )
    response = RegCounter(date="{year}", amount=amount)
    return response


@router.get("/years")
async def count_registrations_per_years_period(
    year_period: YearPeriodParam = Depends(), role: Roles = None
) -> List[RegCounter]:
    collection = await get_registrations_collection()
    start_date, end_date = year_period.date_borders()
    reg_counter = await get_reg_amount_for_period(
        collection, start_date, end_date, role, PeriodFormats.years
    )
    return reg_counter
