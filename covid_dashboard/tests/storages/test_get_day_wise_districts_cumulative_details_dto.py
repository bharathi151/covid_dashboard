import pytest
import datetime

from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.storages.state_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_state_cumulative_details_dto_returns_state_total_cases_dto(district_daily_cases):

    day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

    district_dto = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id = 1,
               day_wise_statistics=day_wise_statistics
        )

    expected_output = DayWiseDistrictTotalCasesDtos(
            districts=[district_dto]
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_districts_cumulative_dto()

    assert expected_output == state_total_cases_dto

@pytest.mark.django_db
def test_get_state_cumulative_details_dto_when_there_is_no_cases_on_some_dates_returns_previous_counts_in_state_total_cases_dto(district_cases):

    day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="22/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

    district_dto = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id = 1,
               day_wise_statistics=day_wise_statistics
        )

    expected_output = DayWiseDistrictTotalCasesDtos(
            districts=[district_dto]
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_districts_cumulative_dto()

    assert expected_output == state_total_cases_dto




@pytest.mark.django_db
def test_get_districts_day_wise_cumulative_details_dto_returns_districts_total_cases_dto_day_wise(daily_cases):

    kadapa_day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]
    kurnool_day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]

    districts_dto = [DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id = 1,
               day_wise_statistics=kadapa_day_wise_statistics
            ),
            DayWiseDistrictTotalCasesDto(
               district_name="Kurnool",
               district_id = 2,
               day_wise_statistics=kurnool_day_wise_statistics
            )
        ]

    expected_output = DayWiseDistrictTotalCasesDtos(
            districts=districts_dto
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_districts_cumulative_dto()

    assert expected_output == state_total_cases_dto
