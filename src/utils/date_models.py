from datetime import datetime, timedelta
import enum
from typing import Union
from pydantic import BaseModel, validator, root_validator


class PeriodFormats(enum.Enum):
    days = "%Y-%m-%d"
    months = "%Y-%m"
    years = "%Y"


class PaginationParam(BaseModel):
    limit: int = 10
    offset: int = 0
    _max_limit = 100

    @validator("limit")
    def validate_limit(cls, v):
        if v < 0 or v > 100:
            raise ValueError(f"Limit should be between 0 and {cls._max_limit}")
        return v

    @validator("offset")
    def validate_offset(cls, v):
        if v < 0:
            raise ValueError(f"Offset should be more than 0")
        return v


class DayParam(BaseModel):
    start_day: str

    @validator("start_day")
    def validate_start_day(cls, v):
        date_format = PeriodFormats.days.value
        try:
            datetime.strptime(v, date_format)
            return v
        except ValueError:
            raise ValueError(f"Invalid date format.Format should be {date_format}")

    def date_borders(self) -> Union[datetime, datetime]:
        start_date = datetime.strptime(self.start_day, PeriodFormats.days.value)
        end_date = start_date + timedelta(days=1)
        return (start_date, end_date)


class DaysPeriodParam(DayParam):
    end_day: str

    @validator("end_day")
    def validate_end_day(cls, v):
        date_format = PeriodFormats.days.value
        try:
            datetime.strptime(v, date_format)
            return v
        except ValueError:
            raise ValueError(f"Invalid date format.Format should be {date_format}")

    def date_borders(self) -> Union[datetime, datetime]:
        start_date = datetime.strptime(self.start_day, PeriodFormats.days.value)
        end_date = datetime.strptime(self.end_day, PeriodFormats.days.value)
        return (start_date, end_date)


class YearMonthParam(BaseModel):
    start_year: int
    start_month: int

    @validator("start_year")
    def validate_year(cls, year):
        if year < 2000 or year > 2100:
            raise ValueError(
                f"Invalid year value.Value must be set between 2000 and 2100"
            )
        return year

    @validator("start_month")
    def validate_month(cls, month):
        if month < 1 or month > 12:
            raise ValueError(f"Invalid month value.Value must be set between 1 and 12")
        return month

    def date_borders(self) -> Union[datetime, datetime]:
        year, month = self.start_year, self.start_month
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        return (start_date, end_date)


class YearMonthPeriodParam(YearMonthParam):
    end_year: int
    end_month: int

    def date_borders(self) -> Union[datetime, datetime]:
        start_date = datetime(self.start_year, self.start_month, 1)
        end_date = datetime(self.end_year, self.end_month, 1)
        return (start_date, end_date)

    @root_validator()
    def validate_period_sequence(cls, field_values):
        super().validate_year(field_values["end_year"])
        super().validate_month(field_values["end_month"])

        start_date = datetime(
            field_values["start_year"], field_values["start_month"], 1
        )
        end_date = datetime(field_values["end_year"], field_values["end_month"], 1)
        if start_date > end_date:
            raise ValueError(f"Invalid period sequence.")
        return field_values


class YearParam(BaseModel):
    start_year: int

    def date_borders(self) -> Union[datetime, datetime]:
        year = self.start_year
        start_date = datetime(year, 1, 1)
        end_date = datetime(year + 1, 1, 1)
        return (start_date, end_date)

    @validator("start_year")
    def validate_year(cls, year):
        if year < 2000 or year > 2100:
            raise ValueError(
                f"Invalid year value.Value must be set between 2000 and 2100"
            )
        return year


class YearPeriodParam(YearParam):
    end_year: int

    def validate_end_year(cls, year):
        return super().validate_year(year)

    def date_borders(self) -> Union[datetime, datetime]:
        start_date = datetime(self.start_year, 1, 1)
        end_date = datetime(self.end_year, 1, 1)
        return (start_date, end_date)

    @root_validator()
    def validate_period_sequence(cls, field_values):
        super().validate_year(field_values["end_year"])

        start_date = datetime(field_values["start_year"], 1, 1)
        end_date = datetime(field_values["end_year"], 1, 1)
        if start_date > end_date:
            raise ValueError(f"Invalid period sequence.")
        return field_values
