from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_mandals_cumulative_report_day_wise_interactor import MandalsCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_mandals_day_wise_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_state_cumulative_response
   ):
        #arrange
        district_id = 1
        expected_output = get_state_cumulative_response
        day_wise_statistics = [
           DayWiseTotalCasesDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            DayWiseTotalCasesDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
            )
        ]

        mandal_dto = DayWiseMandalTotalCasesDto(
               mandal_name="Kadapa",
               mandal_id = 1,
               day_wise_statistics=day_wise_statistics
        )

        mandals_dto = DayWiseMandalTotalCasesDtos(
            mandals=[mandal_dto]
        )

        day_wise_statistics1 = [
           DayWiseCumulativeDto(
               date="20/05/2020",
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_active_cases=7,
               total_deaths=1,
            ),
            DayWiseCumulativeDto(
               date="25/05/2020",
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_active_cases=14,
               total_deaths=2,
            )
        ]

        mandal_cumulative_dto = DayWiseMandalCumulativeDto(
               mandal_name="Kadapa",
               mandal_id = 1,
               day_wise_statistics=day_wise_statistics1
        )

        mandals_cumulative_dto = DayWiseMandalCumulativeDtos(
            mandals=[mandal_cumulative_dto]
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MandalsCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_mandals_cumulative_dto.return_value = mandals_dto
        presenter.get_day_wise_mandals_cumulative_details_dto_response.return_value = expected_output
        #act
        mandals_cumulative_details_dto = interactor.get_day_wise_mandals_cumulative_details(district_id=district_id)
        #assert
        assert mandals_cumulative_details_dto == expected_output
        storage.get_day_wise_mandals_cumulative_dto.assert_called_once_with(district_id=district_id)
        presenter.get_day_wise_mandals_cumulative_details_dto_response.assert_called_once_with(mandals_cumulative_dto)

# def test_get_state_cumulative_report_when_mandal_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
#     create_state,create_mandals
#   ):
#         #arrange
#         expected_output = get_state_cumulative_response
        
#         state_total_cases_dto = StateTotalCasesDto(
#               state_name="AndhraPradesh",
#               total_confirmed_cases=150,
#               total_recovered_cases=55,
#               total_deaths=6,
#               mandals=mandal_total_cases_dtos
#         )

#         mandal_cumulative_dtos = [
#           mandalCumulativeDto(
#               mandal_name="Kadapa",
#               mandal_id=1,
#               total_confirmed_cases=50,
#               total_recovered_cases=45,
#               total_deaths=5,
#               total_active_cases=0
#             ),
#             mandalCumulativeDto(
#               mandal_name="Kurnool",
#               mandal_id=2,
#               total_confirmed_cases=100,
#               total_recovered_cases=10,
#               total_deaths=1,
#               total_active_cases=89
#             )
#         ]
#         state_cumulative_dto = StateCumulativeDto(
#             state_name="AndhraPradesh",
#             total_confirmed_cases=150,
#             total_recovered_cases=55,
#             total_deaths=6,
#             total_active_cases=89
#         )
#         state_cumulative_dtos = StateCumulativeDtos(
#             state=state_cumulative_dto,
#             mandals=mandal_cumulative_dtos
#         )
#         storage = create_autospec(StorageInterface)
#         presenter = create_autospec(PresenterInterface)
#         interactor = StateCumulativeDetailsInteractor(
#             storage=storage, presenter=presenter
#         )

#         storage.get_state_cumulative_details_dto.return_value = state_total_cases_dto
#         presenter.get_state_cumulative_details_dto_response.return_value = expected_output
#         #act
#         state_cumulative_details_dto = interactor.get_state_cumulative_details(till_date=date)
#         #assert
#         assert state_cumulative_details_dto == expected_output
#         storage.get_state_cumulative_details_dto.assert_called_once_with(till_date=date)
#         presenter.get_state_cumulative_details_dto_response.assert_called_once_with(state_cumulative_dtos)

# def test_get_state_cumulative_report_when_state_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
#     get_state_cumulative_response,create_state,create_mandals
#   ):
#         #arrange
#         expected_output = get_state_cumulative_response
#         date = datetime.date(2020,3,15)
#         mandal_total_cases_dtos = [
#           mandalTotalCasesDto(
#               mandal_name="Kadapa",
#               mandal_id=1,
#               total_confirmed_cases=50,
#               total_recovered_cases=45,
#               total_deaths=5,
#             )
#         ]

#         state_total_cases_dto = StateTotalCasesDto(
#               state_name="AndhraPradesh",
#               total_confirmed_cases=50,
#               total_recovered_cases=45,
#               total_deaths=5,
#               mandals=mandal_total_cases_dtos
#         )

#         mandal_cumulative_dtos = [
#           mandalCumulativeDto(
#               mandal_name="Kadapa",
#               mandal_id=1,
#               total_confirmed_cases=50,
#               total_recovered_cases=45,
#               total_deaths=5,
#               total_active_cases=0
#             )
#         ]
#         state_cumulative_dto = StateCumulativeDto(
#             state_name="AndhraPradesh",
#             total_confirmed_cases=50,
#             total_recovered_cases=45,
#             total_deaths=5,
#             total_active_cases=0
#         )
#         state_cumulative_dtos = StateCumulativeDtos(
#             state=state_cumulative_dto,
#             mandals=mandal_cumulative_dtos
#         )
#         storage = create_autospec(StorageInterface)
#         presenter = create_autospec(PresenterInterface)
#         interactor = StateCumulativeDetailsInteractor(
#             storage=storage, presenter=presenter
#         )

#         storage.get_state_cumulative_details_dto.return_value = state_total_cases_dto
#         presenter.get_state_cumulative_details_dto_response.return_value = expected_output
#         #act
#         state_cumulative_details_dto = interactor.get_state_cumulative_details(till_date=date)
#         #assert
#         assert state_cumulative_details_dto == expected_output
#         storage.get_state_cumulative_details_dto.assert_called_once_with(till_date=date)
#         presenter.get_state_cumulative_details_dto_response.assert_called_once_with(state_cumulative_dtos)
