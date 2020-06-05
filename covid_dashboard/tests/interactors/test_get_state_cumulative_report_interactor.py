from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_state_cumulative_report_interactor import StateCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_state_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_state_cumulative_response,create_state,create_districts
   ):
        #arrange
        expected_output = get_state_cumulative_response
        date = "2020-05-30"
        district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
            ),
            DistrictTotalCasesDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
            )
        ]

        state_total_cases_dto = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=1000,
               total_recovered_cases=200,
               total_deaths=60,
               districts=district_total_cases_dtos
        )

        district_cumulative_dtos = [
           DistrictCumulativeDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
               total_active_cases=370
            ),
            DistrictCumulativeDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=500,
               total_recovered_cases=100,
               total_deaths=30,
               total_active_cases=370
            )
        ]
        state_cumulative_dto = StateCumulativeDto(
            state_name="AndhraPradesh",
            total_confirmed_cases=1000,
            total_recovered_cases=200,
            total_deaths=60,
            total_active_cases=740
        )
        state_cumulative_dtos = StateCumulativeDtos(
            state=state_cumulative_dto,
            districts=district_cumulative_dtos
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_state_cumulative_details_dto.return_value = state_total_cases_dto
        presenter.get_state_cumulative_details_dto_response.return_value = expected_output
        #act
        state_cumulative_details_dto = interactor.get_state_cumulative_details(till_date=date)
        #assert
        assert state_cumulative_details_dto == expected_output
        storage.get_state_cumulative_details_dto.assert_called_once_with(till_date=date)
        presenter.get_state_cumulative_details_dto_response.assert_called_once_with(state_cumulative_dtos)

def test_get_state_cumulative_report_when_district_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
    get_state_cumulative_response,create_state,create_districts
   ):
        #arrange
        expected_output = get_state_cumulative_response
        date = datetime.date(2020,3,15)
        district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=50,
               total_recovered_cases=45,
               total_deaths=5,
            ),
            DistrictTotalCasesDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=100,
               total_recovered_cases=10,
               total_deaths=1,
            )
        ]

        state_total_cases_dto = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=150,
               total_recovered_cases=55,
               total_deaths=6,
               districts=district_total_cases_dtos
        )

        district_cumulative_dtos = [
           DistrictCumulativeDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=50,
               total_recovered_cases=45,
               total_deaths=5,
               total_active_cases=0
            ),
            DistrictCumulativeDto(
               district_name="Kurnool",
               district_id=2,
               total_confirmed_cases=100,
               total_recovered_cases=10,
               total_deaths=1,
               total_active_cases=89
            )
        ]
        state_cumulative_dto = StateCumulativeDto(
            state_name="AndhraPradesh",
            total_confirmed_cases=150,
            total_recovered_cases=55,
            total_deaths=6,
            total_active_cases=89
        )
        state_cumulative_dtos = StateCumulativeDtos(
            state=state_cumulative_dto,
            districts=district_cumulative_dtos
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_state_cumulative_details_dto.return_value = state_total_cases_dto
        presenter.get_state_cumulative_details_dto_response.return_value = expected_output
        #act
        state_cumulative_details_dto = interactor.get_state_cumulative_details(till_date=date)
        #assert
        assert state_cumulative_details_dto == expected_output
        storage.get_state_cumulative_details_dto.assert_called_once_with(till_date=date)
        presenter.get_state_cumulative_details_dto_response.assert_called_once_with(state_cumulative_dtos)

def test_get_state_cumulative_report_when_state_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
    get_state_cumulative_response,create_state,create_districts
   ):
        #arrange
        expected_output = get_state_cumulative_response
        date = datetime.date(2020,3,15)
        district_total_cases_dtos = [
           DistrictTotalCasesDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=50,
               total_recovered_cases=45,
               total_deaths=5,
            )
        ]

        state_total_cases_dto = StateTotalCasesDto(
               state_name="AndhraPradesh",
               total_confirmed_cases=50,
               total_recovered_cases=45,
               total_deaths=5,
               districts=district_total_cases_dtos
        )

        district_cumulative_dtos = [
           DistrictCumulativeDto(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=50,
               total_recovered_cases=45,
               total_deaths=5,
               total_active_cases=0
            )
        ]
        state_cumulative_dto = StateCumulativeDto(
            state_name="AndhraPradesh",
            total_confirmed_cases=50,
            total_recovered_cases=45,
            total_deaths=5,
            total_active_cases=0
        )
        state_cumulative_dtos = StateCumulativeDtos(
            state=state_cumulative_dto,
            districts=district_cumulative_dtos
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_state_cumulative_details_dto.return_value = state_total_cases_dto
        presenter.get_state_cumulative_details_dto_response.return_value = expected_output
        #act
        state_cumulative_details_dto = interactor.get_state_cumulative_details(till_date=date)
        #assert
        assert state_cumulative_details_dto == expected_output
        storage.get_state_cumulative_details_dto.assert_called_once_with(till_date=date)
        presenter.get_state_cumulative_details_dto_response.assert_called_once_with(state_cumulative_dtos)
