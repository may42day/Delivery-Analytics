from fastapi import APIRouter, Depends

from utils.date_models import DaysPeriodParam, YearMonthPeriodParam, YearPeriodParam


router = APIRouter()


@router.get("/users/{user_uuid}")
async def get_user_orders(user_uuid: str):
    return True


# with offset
@router.get("/users/top/{year}")
async def get_top_users_per_year(year: str):
    return True


# with offset
@router.get("/users/top/{year}/{month}")
async def get_top_users_per_month(year: str, month: str):
    return True


@router.get("/couriers/{courier_uuid}")
async def get_courier_orders(courier_uuid: str):
    return True


# with offset
@router.get("/couriers/top/{year}")
async def get_top_couriers_per_year(year: str):
    return True


# with offset
@router.get("/couriers/top/{year}/{month}")
async def get_top_couriers_per_month(year: str, month: str):
    return True


@router.get("/count/day/{day}")
async def count_registrations_per_day(
    day: str,
    #   ) -> RegCounter:
    # day = DayParam(start_day=day)
    # collection = await get_registrations_collection()
    # start_date, end_date = day.date_borders()
    # amount = await get_reg_amount_for_specific_date(
    #     collection, start_date, end_date, role
    # )
    # response = RegCounter(date=day.start_day, amount=amount)
    # return response
):
    return True


@router.get("/count/days")
async def count_registrations_per_days_period(
    days_period: DaysPeriodParam = Depends(),
    # ) -> List[RegCounter]:
    # start_date, end_date = days_period.date_borders()
    # collection = await get_registrations_collection()
    # reg_counter = await get_reg_amount_for_period(
    #     collection, start_date, end_date, role, PeriodFormats.days
    # )
    # return reg_counter
):
    return True


@router.get("/count/month/{year}/{month}")
async def count_registrations_per_month(
    year: int,
    month: int
    # ) -> RegCounter:
    #     year_month = YearMonthParam(start_year=year, start_month=month)
    #     collection = await get_registrations_collection()
    #     start_date, end_date = year_month.date_borders()
    #     amount = await get_reg_amount_for_specific_date(
    #         collection, start_date, end_date, role
    #     )
    #     response = RegCounter(date="{year}-{month}", amount=amount)
    #     return response
):
    return True


@router.get("/count/months")
async def count_registrations_per_months_period(
    year_month_period: YearMonthPeriodParam = Depends(),
    # ) -> List[RegCounter]:
    #     collection = await get_registrations_collection()
    #     start_date, end_date = year_month_period.date_borders()
    #     reg_counter = await get_reg_amount_for_period(
    #         collection, start_date, end_date, role, PeriodFormats.months
    #     )
    #     return reg_counter
):
    return True


@router.get("/count/year/{year}")
async def count_registrations_per_year(
    year: int,
    #    ) -> RegCounter:
    # year = YearParam(start_year=year)
    # collection = await get_registrations_collection()
    # start_date, end_date = year.date_borders()
    # amount = await get_reg_amount_for_specific_date(
    #     collection, start_date, end_date, role
    # )
    # response = RegCounter(date="{year}", amount=amount)
    # return response
):
    return True


@router.get("/count/years")
async def count_registrations_per_years_period(
    year_period: YearPeriodParam = Depends(),
    # ) -> List[RegCounter]:
    #     collection = await get_registrations_collection()
    #     start_date, end_date = year_period.date_borders()
    #     reg_counter = await get_reg_amount_for_period(
    #         collection, start_date, end_date, role, PeriodFormats.years
    #     )
    #     return reg_counter
):
    return True
