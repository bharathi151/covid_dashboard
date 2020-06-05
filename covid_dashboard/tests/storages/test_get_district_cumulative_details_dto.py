import pytest
import datetime

from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.storages.district_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_district_cumulative_details_dto_returns_district_total_cases_dto(
    kadapa_mandals_post_cases
    ):
    #arrange
    till_date = datetime.datetime.now().today()
    district_id = 1
    mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]

    expected_output = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
               mandals=mandal_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    district_total_cases_dto = sql_storage.get_district_cumulative_details_dto(
        till_date=till_date, district_id=district_id
    )

    assert expected_output == district_total_cases_dto




@pytest.mark.django_db
def test_get_district_cumulative_details_dto_when_only_some_ditricts_have_cases_and_other_have_no_cases_returns_district_total_cases_dto_with_zero_cases_for_mandals_has_no_cases(rayachoty_cases):
    #arrange
    till_date = datetime.datetime.now().today()
    district_id = 1
    mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            )
        ]

    expected_output = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               mandals=mandal_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    district_total_cases_dto = sql_storage.get_district_cumulative_details_dto(
        till_date=till_date, district_id=district_id)

    assert expected_output == district_total_cases_dto

@pytest.mark.django_db
def test_get_district_cumulative_details_dto_when_district_have_no_cases_returns_district_total_cases_dto_with_zero_cases(create_kadapa_mandals):
    #arrange
    till_date = datetime.datetime.now().today()
    district_id = 1
    mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
            )
        ]

    expected_output = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=0,
               total_recovered_cases=0,
               total_deaths=0,
               mandals=mandal_total_cases_dtos
        )
    sql_storage = StorageImplementation()

    #act
    district_total_cases_dto = sql_storage.get_district_cumulative_details_dto(
        till_date=till_date, district_id=district_id
    )

    #assert
    assert expected_output == district_total_cases_dto