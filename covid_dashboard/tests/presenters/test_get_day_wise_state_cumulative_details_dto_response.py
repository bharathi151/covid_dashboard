import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output = {
        "state_name": "AndhraPradesh",
        "day_wise_statistics": [
            {
                "date": datetime.date(2020,5,20),
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            },
            {
                "date": datetime.date(2020,5,25),
                "total_confirmed_cases": 20,
                "total_recovered_cases": 4,
                "total_deaths": 2,
                "total_active_cases": 14
            }
        ] 
    }

    day_wise_statistics = [
         DayWiseStateCumulativeDto(
            date=datetime.date(2020,5,20),
            total_confirmed_cases=10,
            total_recovered_cases=2,
            total_deaths=1,
            total_active_cases=7
        ),
        DayWiseStateCumulativeDto(
            date=datetime.date(2020,5,25),
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            total_active_cases=14
        )
    ]

    day_wise_state_cumulative_data = DayWiseStateCumulativeDtos(
        state_name="AndhraPradesh",
        day_wise_statistics=day_wise_statistics
    )

    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_day_wise_state_cumulative_details_dto_response(
        state_cumulative_dto=day_wise_state_cumulative_data
    )

    assert cumulative_dict == expected_output
