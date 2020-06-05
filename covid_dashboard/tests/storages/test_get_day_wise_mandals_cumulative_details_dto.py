import pytest
import datetime

from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.storages.district_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_state_cumulative_details_dto_returns_state_total_cases_dto(district_daily_cases):

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
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

    mandal_dto = DayWiseMandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id = 1,
               day_wise_statistics=day_wise_statistics
        )

    expected_output = DayWiseMandalTotalCasesDtos(
            mandals=[mandal_dto]
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_mandals_cumulative_dto(district_id=district_id)

    assert expected_output == state_total_cases_dto

@pytest.mark.django_db
def test_get_state_cumulative_details_dto_when_there_is_no_cases_on_some_dates_returns_previous_counts_in_state_total_cases_dto(district_cases):

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

    mandal_dto = DayWiseMandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id = 1,
               day_wise_statistics=day_wise_statistics
        )

    expected_output = DayWiseMandalTotalCasesDtos(
            mandals=[mandal_dto]
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_mandals_cumulative_dto(district_id=district_id)

    assert expected_output == state_total_cases_dto




@pytest.mark.django_db
def test_get_mandals_day_wise_cumulative_details_dto_returns_mandals_total_cases_dto_day_wise(mandals_cases):
    district_id = 1
    rct_day_wise_statistics = [
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
    gvl_day_wise_statistics = [
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

    mandals_dto = [DayWiseMandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id = 1,
               day_wise_statistics=rct_day_wise_statistics
            ),
            DayWiseMandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id = 2,
               day_wise_statistics=gvl_day_wise_statistics
            )
        ]

    expected_output = DayWiseMandalTotalCasesDtos(
            mandals=mandals_dto
        )

    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_day_wise_mandals_cumulative_dto(district_id=district_id)

    assert expected_output == state_total_cases_dto
