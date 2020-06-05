from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_district_daily_report_day_wise_interactor import DistrictDailyDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_district_daily_report_when_there_is_active_cases_return_daily_details_with_total_active_cases(
    get_district_cumulative_response
   ):
        #arrange
        till_date = "2020-05-22"
        district_id = 1
        expected_output = get_district_cumulative_response
        day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

        storage_dto = DayWiseDistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               day_wise_statistics=day_wise_statistics
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictDailyDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_district_daily_dto.return_value = storage_dto
        presenter.get_day_wise_district_daily_details_dto_response.return_value = expected_output
        #act
        district_daily_details_dto = interactor.get_day_wise_district_daily_details(till_date=till_date, district_id=district_id)
        #assert
        assert district_daily_details_dto == expected_output
        storage.get_day_wise_district_daily_dto.assert_called_once_with(till_date=till_date, district_id=district_id)
        presenter.get_day_wise_district_daily_details_dto_response.assert_called_once_with(district_daily_dto=storage_dto)
