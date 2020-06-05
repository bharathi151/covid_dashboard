from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_state_cumulative_report_day_wise_interactor import StateCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_state_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_state_cumulative_response
   ):
        #arrange
        expected_output = get_state_cumulative_response
        day_wise_statistics = [
           DayWiseStateTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseStateTotalCasesDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

        storage_dto = DayWiseStateTotalCasesDtos(
               state_name="AndhraPradesh",
               day_wise_statistics=day_wise_statistics
        )

        day_wise_statistics1 = [
           DayWiseStateCumulativeDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_active_cases=7,
               total_deaths=1,
            ),
            DayWiseStateCumulativeDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_active_cases=14,
               total_deaths=2,
            )
        ]

        interactor_dto = DayWiseStateCumulativeDtos(
               state_name="AndhraPradesh",
               day_wise_statistics=day_wise_statistics1
        )


        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_state_cumulative_dto.return_value = storage_dto
        presenter.get_day_wise_state_cumulative_details_dto_response.return_value = expected_output
        #act
        state_cumulative_details_dto = interactor.get_day_wise_state_cumulative_details()
        #assert
        assert state_cumulative_details_dto == expected_output
        storage.get_day_wise_state_cumulative_dto.assert_called_once_with()
        presenter.get_day_wise_state_cumulative_details_dto_response.assert_called_once_with(interactor_dto)

def test_get_state_cumulative_report_when_there_is_no_active_cases_return_cumulative_details_with_zero_total_active_cases(
    get_state_cumulative_response
   ):
        #arrange
        expected_output = get_state_cumulative_response
        day_wise_statistics = [
           DayWiseStateTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_deaths=2,
            ),
            DayWiseStateTotalCasesDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=16,
               total_deaths=4,
            )
        ]

        storage_dto = DayWiseStateTotalCasesDtos(
               state_name="AndhraPradesh",
               day_wise_statistics=day_wise_statistics
        )

        day_wise_statistics1 = [
           DayWiseStateCumulativeDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_active_cases=0,
               total_deaths=2,
            ),
            DayWiseStateCumulativeDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=16,
               total_active_cases=0,
               total_deaths=4,
            )
        ]

        interactor_dto = DayWiseStateCumulativeDtos(
               state_name="AndhraPradesh",
               day_wise_statistics=day_wise_statistics1
        )


        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_state_cumulative_dto.return_value = storage_dto
        presenter.get_day_wise_state_cumulative_details_dto_response.return_value = expected_output
        #act
        state_cumulative_details_dto = interactor.get_day_wise_state_cumulative_details()
        #assert
        assert state_cumulative_details_dto == expected_output
        storage.get_day_wise_state_cumulative_dto.assert_called_once_with()
        presenter.get_day_wise_state_cumulative_details_dto_response.assert_called_once_with(interactor_dto)
