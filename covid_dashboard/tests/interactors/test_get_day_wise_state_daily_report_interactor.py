from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_state_daily_report_day_wise_interactor import StateDailyDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_state_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_state_cumulative_response
   ):
        #arrange
        till_date = "2020-05-22"
        expected_output = get_state_cumulative_response
        day_wise_statistics = [
           DayWiseStateTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseStateTotalCasesDto(
               date="21/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

        storage_dto = DayWiseStateTotalCasesDtos(
               state_name="AndhraPradesh",
               day_wise_statistics=day_wise_statistics
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateDailyDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_state_daily_dto.return_value = storage_dto
        presenter.get_day_wise_state_daily_details_dto_response.return_value = expected_output
        #act
        state_daily_details_dto = interactor.get_day_wise_state_daily_details(till_date=till_date)
        #assert
        assert state_daily_details_dto == expected_output
        storage.get_day_wise_state_daily_dto.assert_called_once_with(till_date=till_date)
        presenter.get_day_wise_state_daily_details_dto_response.assert_called_once_with(state_daily_dto=storage_dto)
