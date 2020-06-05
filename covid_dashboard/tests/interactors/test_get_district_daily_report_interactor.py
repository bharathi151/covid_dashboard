from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_district_daily_report_interactor import DistrictDailyDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_district_daily_report_when_there_is_active_cases_return_daily_details_with_total_active_cases(
    get_district_cumulative_response
   ):
        #arrange
        district_id = 1
        expected_output = get_district_cumulative_response
        date = "2020-05-30"
        mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
            )
        ]

        district_total_cases_dto = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=1000,
               total_recovered_cases=20,
               total_deaths=60,
               mandals=mandal_total_cases_dtos
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictDailyDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_district_daily_details_dto.return_value = district_total_cases_dto
        presenter.get_district_daily_details_dto_response.return_value = expected_output
        #act
        district_daily_details_dto = interactor.get_district_daily_details(till_date=date, district_id=district_id)
        #assert
        assert district_daily_details_dto == expected_output
        storage.get_district_daily_details_dto.assert_called_once_with(date=date, district_id=district_id)
        presenter.get_district_daily_details_dto_response.assert_called_once_with(district_total_cases_dto)
