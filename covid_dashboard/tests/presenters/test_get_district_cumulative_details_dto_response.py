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
        "total_active_cases": 14,
        "mandals": [
            {
                "mandal_name": "Rayachoty",
                "mandal_id": 1,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            },
            {
                "mandal_name": "Gaaliveedu",
                "mandal_id": 2,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            }
        ]
    }
    mandal_cumulative_dtos = [
           MandalCumulativeDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            ),
            MandalCumulativeDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            )
        ]
    district_cumulative_dto = DistrictCumulativeDto(
            district_name="Kadapa",
            district_id=1,
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            total_active_cases=14
        )
    district_cumulative_dtos = DistrictCumulativeDtos(
            district=district_cumulative_dto,
            mandals=mandal_cumulative_dtos
        )
    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_district_cumulative_details_dto_response(
        district_cumulative_dto=district_cumulative_dtos
    )

    assert cumulative_dict["mandals"] == expected_output["mandals"]
