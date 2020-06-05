import pytest
import datetime

from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.storages.state_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_state_cumulative_details_dto_returns_state_total_cases_dto(post_cases):
    till_date = datetime.datetime.now().today()
    district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DistrictTotalCasesDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]

    expected_output = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
               districts=district_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_state_cumulative_details_dto(
        till_date=till_date
    )

    assert expected_output == state_total_cases_dto


@pytest.mark.django_db
def test_get_state_cumulative_details_dto_when_cases_posted_on_same_date_for_different_mandals_returns_state_total_cases_dto(kadapa_cases):
    till_date = datetime.datetime.now().today()
    district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

    expected_output = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
               districts=district_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_state_cumulative_details_dto(
        till_date=till_date
    )

    assert expected_output == state_total_cases_dto




@pytest.mark.django_db
def test_get_state_cumulative_details_dto_when_only_some_ditricts_have_cases_and_other_have_no_cases_returns_state_total_cases_dto_with_zero_cases_for_districts_has_no_cases(cases):
    till_date = datetime.datetime.now().today()
    district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DistrictTotalCasesDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            )
        ]

    expected_output = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               districts=district_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_state_cumulative_details_dto(
        till_date=till_date
    )

    assert expected_output == state_total_cases_dto

@pytest.mark.django_db
def test_get_state_cumulative_details_dto_when_state_have_no_cases_returns_state_total_cases_dto_with_zero_cases(create_mandals):
    till_date = datetime.datetime.now().today()
    district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            ),
            DistrictTotalCasesDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            )
        ]

    expected_output = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
               districts=district_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    state_total_cases_dto = sql_storage.get_state_cumulative_details_dto(
        till_date=till_date
    )

    assert expected_output == state_total_cases_dto