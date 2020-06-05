import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output =[ {
        "mandal_name": "Rayachoty",
        "mandal_id": 1,
        "day_wise_statistics": [
            {
                "date": "20/05/2020",
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            },
            {
                "date":"25/05/2020",
                "total_confirmed_cases": 20,
                "total_recovered_cases": 4,
                "total_deaths": 2,
                "total_active_cases": 14
            }
        ] 
    }
    ]
    day_wise_statistics = [
         DayWiseCumulativeDto(
            date="20/05/2020",
            total_confirmed_cases=10,
            total_recovered_cases=2,
            total_deaths=1,
            total_active_cases=7
        ),
        DayWiseCumulativeDto(
            date="25/05/2020",
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            total_active_cases=14
        )
    ]

    mandal_cumulative_data = DayWiseMandalCumulativeDto(
            mandal_name="Rayachoty",
            mandal_id=1,
            day_wise_statistics=day_wise_statistics
        )
    mandals_cumulative_dto = DayWiseMandalCumulativeDtos(
        mandals=[mandal_cumulative_data]
    )

    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_day_wise_mandals_cumulative_details_dto_response(
        mandals_cumulative_dto=mandals_cumulative_dto
    )

    assert cumulative_dict == expected_output
