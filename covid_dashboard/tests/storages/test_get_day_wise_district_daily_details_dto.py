import pytest
import datetime

from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.storages.district_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_day_wise_district_daily_details_dto_returns_district_total_cases_dto(daily_cases):

    district_id = 1
    till_date = datetime.date(2020,5,21)
    day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            )
        ]

    expected_output = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               day_wise_statistics=day_wise_statistics
        )
    sql_storage = StorageImplementation()

    district_total_cases_dto = sql_storage.get_day_wise_district_daily_dto(till_date=till_date, district_id=district_id)

    assert expected_output == district_total_cases_dto

@pytest.mark.django_db
def test_get_day_wise_district_daily_details_dto_when_there_is_no_case_for_dates_returns_district_total_cases_dto_with_previous_data_for_those_dates(post_cases):

    till_date = datetime.date(2020,5,22)
    district_id = 1
    day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            ),
            DayWiseTotalCasesDto(
               date="22/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]

    expected_output = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               day_wise_statistics=day_wise_statistics
        )
    sql_storage = StorageImplementation()

    district_total_cases_dto = sql_storage.get_day_wise_district_daily_dto(
        till_date=till_date, district_id=district_id
    )

    assert expected_output == district_total_cases_dto

@pytest.mark.django_db
def test_get_day_wise_district_daily_details_dto_when_cases_registered_for_two_mandals_on_same_dates_returns_district_total_cases_dto_with_for_that_date(kadapa_cases):

    till_date = datetime.date(2020,5,20)
    district_id = 1
    day_wise_statistics = [
            DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2
            )
        ]

    expected_output = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               day_wise_statistics=day_wise_statistics
        )
    sql_storage = StorageImplementation()

    district_total_cases_dto = sql_storage.get_day_wise_district_daily_dto(till_date=till_date, district_id=district_id)

    assert expected_output == district_total_cases_dto
