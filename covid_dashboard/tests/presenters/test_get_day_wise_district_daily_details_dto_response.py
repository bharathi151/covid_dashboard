import datetime

from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation



def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict():

    expected_output = {
        "district_name": "Kadapa",
        "district_id":1,
        "day_wise_statistics": [
            {
                "date": datetime.date(2020,5,20),
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
            },
            {
                "date": datetime.date(2020,5,21),
                "total_confirmed_cases": 20,
                "total_recovered_cases": 4,
                "total_deaths": 2
            }
        ] 
    }

    day_wise_statistics = [
         DayWiseTotalCasesDto(
            date=datetime.date(2020,5,20),
            total_confirmed_cases=10,
            total_recovered_cases=2,
            total_deaths=1,
        ),
        DayWiseTotalCasesDto(
            date=datetime.date(2020,5,21),
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2
        )
    ]

    day_wise_district_daily_data = DayWiseDistrictTotalCasesDto(
        district_name="Kadapa",
        district_id=1,
        day_wise_statistics=day_wise_statistics
    )

    json_presenter = PresenterImplementation()

    daily_dict = json_presenter.get_day_wise_district_daily_details_dto_response(
        district_daily_dto=day_wise_district_daily_data
    )

    assert daily_dict == expected_output
