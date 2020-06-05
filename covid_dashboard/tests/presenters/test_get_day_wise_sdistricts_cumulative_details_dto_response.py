import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output =[ {
        "district_name": "Kadapa",
        "district_id": 1,
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

    district_cumulative_data = DayWiseDistrictCumulativeDto(
            district_name="Kadapa",
            district_id=1,
            day_wise_statistics=day_wise_statistics
        )
    districts_cumulative_dto = DayWiseDistrictCumulativeDtos(
        districts=[district_cumulative_data]
    )

    json_presenter = PresenterImplementation()

    cumulative_dict = json_presenter.get_day_wise_districts_cumulative_details_dto_response(
        districts_cumulative_dto=districts_cumulative_dto
    )

    assert cumulative_dict == expected_output
