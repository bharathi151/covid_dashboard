from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_district_cumulative_report_interactor import DistrictCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_district_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_district_cumulative_response,create_districts, create_kadapa_mandals
   ):
        #arrange
        expected_output = get_district_cumulative_response
        date = "2020-05-30"
        district_id = 1
        mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
            )
        ]

        district_total_cases_dto = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=20,
               total_recovered_cases=4,
               total_deaths=2,
               mandals=mandal_total_cases_dtos
        )

        mandal_cumulative_dtos = [
           MandalCumulativeDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            ),
            MandalCumulativeDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=2,
               total_deaths=1,
               total_active_cases=7
            )
        ]
        district_cumulative_dto = DistrictCumulativeDto(
            district_name="Kadapa",
            district_id=1,
            total_confirmed_cases=10,
            total_recovered_cases=2,
            total_deaths=1,
            total_active_cases=7
        )
        district_cumulative_dtos = DistrictCumulativeDtos(
            district=district_cumulative_dto,
            mandals=mandal_cumulative_dtos
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_district_cumulative_details_dto.return_value = district_total_cases_dto
        presenter.get_district_cumulative_details_dto_response.return_value = expected_output

        #act
        district_cumulative_details_dto = interactor. \
            get_district_cumulative_details(
                till_date=date, district_id=district_id
            )

        #assert
        assert district_cumulative_details_dto == expected_output
        storage.get_district_cumulative_details_dto.assert_called_once_with(
            till_date=date,district_id=district_id
            )
        presenter.get_district_cumulative_details_dto_response.assert_called_once_with(district_cumulative_details_dto
            )

# def test_get_District_cumulative_report_when_mandal_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
#     get_District_cumulative_response,create_District,create_mandals
#   ):
#         #arrange
#         expected_output = get_District_cumulative_response
#         date = datetime.date(2020,3,15)
#         mandal_total_cases_dtos = [
#           mandalTotalCasesDto(
#               mandal_name="Kadapa",
#               mandal_id=1,
#               total_confirmed_cases=50,
#               total_recovered_cases=45,
#               total_deaths=5,
#             ),
#             mandalTotalCasesDto(
#               mandal_name="Kurnool",
#               mandal_id=2,
#               total_confirmed_cases=100,
#               total_recovered_cases=10,
#               total_deaths=1,
#             )
#         ]

#         District_total_cases_dto = DistrictTotalCasesDto(
#               District_name="AndhraPradesh",
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
#         District_cumulative_dto = DistrictCumulativeDto(
#             District_name="AndhraPradesh",
#             total_confirmed_cases=150,
#             total_recovered_cases=55,
#             total_deaths=6,
#             total_active_cases=89
#         )
#         District_cumulative_dtos = DistrictCumulativeDtos(
#             District=District_cumulative_dto,
#             mandals=mandal_cumulative_dtos
#         )
#         storage = create_autospec(StorageInterface)
#         presenter = create_autospec(PresenterInterface)
#         interactor = DistrictCumulativeDetailsInteractor(
#             storage=storage, presenter=presenter
#         )

#         storage.get_District_cumulative_details_dto.return_value = District_total_cases_dto
#         presenter.get_District_cumulative_details_dto_response.return_value = expected_output
#         #act
#         District_cumulative_details_dto = interactor.get_District_cumulative_details(till_date=date)
#         #assert
#         assert District_cumulative_details_dto == expected_output
#         storage.get_District_cumulative_details_dto.assert_called_once_with(till_date=date)
#         presenter.get_District_cumulative_details_dto_response.assert_called_once_with(District_cumulative_dtos)

# def test_get_District_cumulative_report_when_District_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
#     get_District_cumulative_response,create_District,create_mandals
#   ):
#         #arrange
#         expected_output = get_District_cumulative_response
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

#         District_total_cases_dto = DistrictTotalCasesDto(
#               District_name="AndhraPradesh",
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
#         District_cumulative_dto = DistrictCumulativeDto(
#             District_name="AndhraPradesh",
#             total_confirmed_cases=50,
#             total_recovered_cases=45,
#             total_deaths=5,
#             total_active_cases=0
#         )
#         District_cumulative_dtos = DistrictCumulativeDtos(
#             District=District_cumulative_dto,
#             mandals=mandal_cumulative_dtos
#         )
#         storage = create_autospec(StorageInterface)
#         presenter = create_autospec(PresenterInterface)
#         interactor = DistrictCumulativeDetailsInteractor(
#             storage=storage, presenter=presenter
#         )

#         storage.get_District_cumulative_details_dto.return_value = District_total_cases_dto
#         presenter.get_District_cumulative_details_dto_response.return_value = expected_output
#         #act
#         District_cumulative_details_dto = interactor.get_District_cumulative_details(till_date=date)
#         #assert
#         assert District_cumulative_details_dto == expected_output
#         storage.get_District_cumulative_details_dto.assert_called_once_with(till_date=date)
#         presenter.get_District_cumulative_details_dto_response.assert_called_once_with(District_cumulative_dtos)
