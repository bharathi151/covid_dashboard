import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output = {
        "state_name": "AndhraPradesh",
        "total_confirmed_cases": 20,
        "total_recovered_cases": 4,
        "total_deaths": 2,
        "total_active_cases": 14,
        "districts": [
            {
                "district_name": "Kadapa",
                "district_id": 1,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            },
            {
                "district_name": "Kurnool",
                "district_id": 2,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            }
        ]
    }
    district_cumulative_dtos = [
           DistrictCumulativeDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            ),
            DistrictCumulativeDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            )
        ]
    state_cumulative_dto = StateCumulativeDto(
            state_name="AndhraPradesh",
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            total_active_cases=14
        )
    state_cumulative_dtos = StateCumulativeDtos(
            state=state_cumulative_dto,
            districts=district_cumulative_dtos
        )
    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_state_cumulative_details_dto_response(
        state_cumulative_dto=state_cumulative_dtos
    )

    assert cumulative_dict == expected_output
