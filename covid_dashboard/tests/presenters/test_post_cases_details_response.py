from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.interactors.storages.dtos import CasesDetailsDto

def test_post_cases_details_response_return_stats_dict():

    expected_dict = {
        "mandal_id": 1,
        "date": "25/05/2020",
        "total_confirmed_cases": 2,
        "total_recovered_cases": 1,
        "total_deaths":0
    }
    stats_dto = CasesDetailsDto(
        mandal_id=1,
        date="25/05/2020",
        total_confirmed_cases=2,
        total_recovered_cases=1,
        total_deaths=0
    )
    json_presenter = PresenterImplementation()

    stats_dict = json_presenter.post_cases_details_response(
        stats_dto=stats_dto
    )

    assert stats_dict == expected_dict