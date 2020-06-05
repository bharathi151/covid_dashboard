import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output = {
        "district_name": "Kadapa",
        "district_id": 1,
        "total_confirmed_cases": 20,
        "total_recovered_cases": 4,
        "total_deaths": 2,
        "mandals": [
            {
                "mandal_name": "Rayochoty",
                "mandal_id": 1,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1
            },
            {
                "mandal_name": "Gaaliveedu",
                "mandal_id": 2,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1
            }
        ]
    }
    mandal_daily_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayochoty",
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
    district_daily_dto = DistrictTotalCasesDtos(
            district_name="Kadapa",
            district_id=1,
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            mandals=mandal_daily_dtos
        )

    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_district_daily_details_dto_response(
        district_daily_dto=district_daily_dto
    )

    assert cumulative_dict == expected_output
