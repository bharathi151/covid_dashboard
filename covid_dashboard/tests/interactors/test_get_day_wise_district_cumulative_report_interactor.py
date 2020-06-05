from unittest.mock import create_autospec
import datetime

from covid_dashboard.interactors.get_district_cumulative_report_day_wise_interactor import DistrictCumulativeDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.storages.dtos import *


def test_get_district_cumulative_report_when_there_is_active_cases_return_cumulative_details_with_total_active_cases(
    get_district_cumulative_response
  ):
        #arrange
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

        cumulative_day_wise_statistics = [
          DayWiseCumulativeDto(
              date="20/05/2020",
              total_confirmed_cases=10,
              total_recovered_cases=2,
              total_deaths=1,
              total_active_cases=7
            ),
            DayWiseCumulativeDto(
              date="21/05/2020",
              total_confirmed_cases=20,
              total_recovered_cases=4,
              total_deaths=2,
              total_active_cases=14
            )
        ]

        interactor_dto = DayWiseDistrictCumulativeDto(
              district_name="Kadapa",
              district_id=1,
              day_wise_statistics=cumulative_day_wise_statistics
        )


        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_district_cumulative_dto.return_value = storage_dto
        presenter.get_day_wise_district_cumulative_details_dto_response.return_value = expected_output
        #act
        district_cumulative_details_dto = interactor.get_day_wise_district_cumulative_details(district_id=district_id)
        #assert
        assert district_cumulative_details_dto == expected_output
        storage.get_day_wise_district_cumulative_dto.assert_called_once_with(district_id=district_id)
        presenter.get_day_wise_district_cumulative_details_dto_response.assert_called_once_with(district_cumulative_dto=interactor_dto)

def test_get_district_cumulative_report_when_there_is_no_active_cases_return_cumulative_details_with_zero_total_active_cases(
    get_district_cumulative_response
  ):
        #arrange
        district_id = 1
        expected_output = get_district_cumulative_response
        day_wise_statistics = [
          DayWiseTotalCasesDto(
              date="20/05/2020",
              total_confirmed_cases=10,
              total_recovered_cases=8,
              total_deaths=2,
            ),
            DayWiseTotalCasesDto(
              date="21/05/2020",
              total_confirmed_cases=20,
              total_recovered_cases=16,
              total_deaths=4,
            )
        ]

        storage_dto = DayWiseDistrictTotalCasesDto(
              district_name="Kadapa",
              district_id=1,
              day_wise_statistics=day_wise_statistics
        )

        cumulative_day_wise_statistics = [
          DayWiseCumulativeDto(
              date="20/05/2020",
              total_confirmed_cases=10,
              total_recovered_cases=8,
              total_deaths=2,
              total_active_cases=0
            ),
            DayWiseCumulativeDto(
              date="21/05/2020",
              total_confirmed_cases=20,
              total_recovered_cases=16,
              total_deaths=4,
              total_active_cases=0
            )
        ]

        interactor_dto = DayWiseDistrictCumulativeDto(
              district_name="Kadapa",
              district_id=1,
              day_wise_statistics=cumulative_day_wise_statistics
        )


        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DistrictCumulativeDetailsInteractor(
            storage=storage, presenter=presenter
        )

        storage.get_day_wise_district_cumulative_dto.return_value = storage_dto
        presenter.get_day_wise_district_cumulative_details_dto_response.return_value = expected_output
        #act
        district_cumulative_details_dto = interactor.get_day_wise_district_cumulative_details(district_id=district_id)
        #assert
        assert district_cumulative_details_dto == expected_output
        storage.get_day_wise_district_cumulative_dto.assert_called_once_with(district_id=district_id)
        presenter.get_day_wise_district_cumulative_details_dto_response.assert_called_once_with(district_cumulative_dto=interactor_dto)
