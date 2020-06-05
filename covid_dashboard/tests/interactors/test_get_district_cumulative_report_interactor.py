from unittest.mock import create_autospec
import datetime
import pytest

from django_swagger_utils.drf_server.exceptions import NotFound
from covid_dashboard.interactors.get_district_cumulative_report_interactor import DistrictCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_district_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_district_cumulative_response
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
            total_confirmed_cases=20,
            total_recovered_cases=4,
            total_deaths=2,
            total_active_cases=14
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

        storage.is_valid_district_id.return_value = True
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
        presenter.get_district_cumulative_details_dto_response.assert_called_once_with(
            district_cumulative_dto=district_cumulative_dtos
            )

def test_get_district_cumulative_report_when_mandal_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
    get_district_cumulative_response
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
               total_recovered_cases=8,
               total_deaths=2,
            )
        ]

        district_total_cases_dto = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=20,
               total_recovered_cases=10,
               total_deaths=3,
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
               total_recovered_cases=8,
               total_deaths=2,
               total_active_cases=0
            )
        ]
        district_cumulative_dto = DistrictCumulativeDto(
            district_name="Kadapa",
            district_id=1,
            total_confirmed_cases=20,
            total_recovered_cases=10,
            total_deaths=3,
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

        storage.is_valid_district_id.return_value = True
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
        presenter.get_district_cumulative_details_dto_response.assert_called_once_with(
            district_cumulative_dto=district_cumulative_dtos
            )

def test_get_district_cumulative_report_when_district_has_no_active_cases_return_cumulative_details_with_zero_active_cases(
        get_district_cumulative_response
  ):
        #arrage
        expected_output = get_district_cumulative_response
        date = "2020-05-30"
        district_id = 1
        mandal_total_cases_dtos = [
           MandalTotalCasesDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_deaths=2,
            ),
            MandalTotalCasesDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_deaths=2,
            )
        ]

        district_total_cases_dto = DistrictTotalCasesDtos(
               district_name="Kadapa",
               district_id=1,
               total_confirmed_cases=20,
               total_recovered_cases=16,
               total_deaths=4,
               mandals=mandal_total_cases_dtos
        )

        mandal_cumulative_dtos = [
           MandalCumulativeDto(
               mandal_name="Rayachoty",
               mandal_id=1,
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_deaths=2,
               total_active_cases=0
            ),
            MandalCumulativeDto(
               mandal_name="Gaaliveedu",
               mandal_id=2,
               total_confirmed_cases=10,
               total_recovered_cases=8,
               total_deaths=2,
               total_active_cases=0
            )
        ]
        district_cumulative_dto = DistrictCumulativeDto(
            district_name="Kadapa",
            district_id=1,
            total_confirmed_cases=20,
            total_recovered_cases=16,
            total_deaths=4,
            total_active_cases=0
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

        storage.is_valid_district_id.return_value = True
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
        presenter.get_district_cumulative_details_dto_response.assert_called_once_with(
            district_cumulative_dto=district_cumulative_dtos
            )

def test_district_cumulative_details_dto_when_given_invalid_district_id_raise_inavlid_dtrict_exception():
        #arrange
        date = "2020-05-30"
        district_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.is_valid_district_id.return_value = False
        presenter.raise_invalid_district_id_exception.side_effect = NotFound

        #act
        with pytest.raises(NotFound):
            interactor.get_district_cumulative_details(
                till_date=date, district_id=district_id
            )

        #assert
        storage.is_valid_district_id.assert_called_once_with(
            district_id=district_id
        )
        presenter.raise_invalid_district_id_exception.assert_called_once()
