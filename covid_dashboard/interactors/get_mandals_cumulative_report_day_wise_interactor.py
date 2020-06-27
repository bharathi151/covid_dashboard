from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class MandalsCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_mandals_cumulative_details(self, district_id):

        is_invalid_district_id = not self.storage.is_valid_district_id(
            district_id=district_id
        )
        if is_invalid_district_id:
            self.presenter.raise_invalid_district_id_exception()
            return

        cumulative_dto = self.storage.\
            get_day_wise_mandals_cumulative_dto(district_id=district_id)
        mandals_dtos = self._get_mandals_dtos(cumulative_dto=cumulative_dto)
        mandals_cumulative_dtos = DayWiseMandalCumulativeDtos(
            mandals=mandals_dtos
        )
        response = self.presenter.get_day_wise_mandals_cumulative_details_dto_response(
            mandals_cumulative_dto=mandals_cumulative_dtos
        )
        return response


    def _get_total_active_cases(self,cumulative_dto):
        total_confirmed_cases = cumulative_dto.total_confirmed_cases
        total_deaths = cumulative_dto.total_deaths
        total_recovered_cases = cumulative_dto.total_recovered_cases
        total_active_cases = total_confirmed_cases - (
                total_deaths + total_recovered_cases
            )
        invalid_active_cases = not (total_active_cases >= 0)
        if invalid_active_cases:
            total_active_cases = 0
        return total_active_cases

    def _get_mandals_dtos(self, cumulative_dto):
        mandals = []
        for mandal in cumulative_dto.mandals:
            mandals.append(
                self._get_mandal_stats_dtos(mandal=mandal)
            )
        return mandals

    def _get_mandal_stats_dtos(self, mandal):
        day_wise_statistics = []
        for mandal_dto in mandal.day_wise_statistics:
            total_active_cases = self._get_total_active_cases(mandal_dto)
            day_wise_statistics.append(
                self._get_day_wise_cumulative_mandal_dto(
                    mandal=mandal_dto, total_active_cases=total_active_cases
                )
            )
        mandal_dtos = DayWiseMandalCumulativeDto(
            mandal_name=mandal.mandal_name,
            mandal_id=mandal.mandal_id,
            day_wise_statistics=day_wise_statistics
        )
        return mandal_dtos


    def _get_day_wise_cumulative_mandal_dto(self, mandal, total_active_cases):
        state_dto = DayWiseCumulativeDto(
            total_recovered_cases=mandal.total_recovered_cases,
            total_confirmed_cases=mandal.total_confirmed_cases,
            total_deaths=mandal.total_deaths,
            total_active_cases=total_active_cases,
            date=mandal.date
        )
        return state_dto