import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output = {
        "state_name": "AndhraPradesh",
        "total_confirmed_cases": 20,
        "total_recovered_cases": 4,
        "total_deaths": 2,
        "districts": [
            {
                "district_name": "Kadapa",
                "district_id": 1,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1
            },
            {
                "district_name": "Kurnool",
                "district_id": 2,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1
            }
        ]
    }
    district_daily_dtos = [
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
    state_daily_dto = StateTotalCasesDto(
            state_name="AndhraPradesh",
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            districts=district_daily_dtos
        )

    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_state_daily_details_dto_response(
        state_daily_dto=state_daily_dto
    )

    assert cumulative_dict == expected_output
