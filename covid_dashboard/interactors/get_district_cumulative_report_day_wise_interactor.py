from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class DistrictCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_district_cumulative_details(self, district_id):
        is_invalid_district_id = not self.storage.is_valid_district_id(
            district_id=district_id
        )
        if is_invalid_district_id:
            self.presenter.raise_invalid_district_id_exception()
            return

        cumulative_dto = self.storage.get_day_wise_district_cumulative_dto(
            district_id=district_id
        )

        district_dtos = self._get_district_dtos(cumulative_dto=cumulative_dto)
        district_cumulative_dtos = DayWiseDistrictCumulativeDto(
            district_name=cumulative_dto.district_name,
            district_id=cumulative_dto.district_id,
            day_wise_statistics=district_dtos
            ) 

        response = self.presenter.get_day_wise_district_cumulative_details_dto_response(
            district_cumulative_dto=district_cumulative_dtos
        )

        return response


    def _get_total_active_cases(self,cumulative_dto):
        total_confirmed_cases = cumulative_dto.total_confirmed_cases
        total_deaths = cumulative_dto.total_deaths
        total_recovered_cases = cumulative_dto.total_recovered_cases
        total_active_cases = total_confirmed_cases - (
                total_deaths + total_recovered_cases
            )
        return total_active_cases

    def _get_district_dtos(self, cumulative_dto):
        district_dtos = []
        for district in cumulative_dto.day_wise_statistics:
            total_active_cases = self._get_total_active_cases(district)
            district_dtos.append(
                self._get_day_wise_cumulative_district_dto(
                    district=district, total_active_cases=total_active_cases
                )
            )
        return district_dtos


    def _get_day_wise_cumulative_district_dto(self, district, total_active_cases):
        district_dto = DayWiseCumulativeDto(
            total_recovered_cases=district.total_recovered_cases,
            total_confirmed_cases=district.total_confirmed_cases,
            total_deaths=district.total_deaths,
            total_active_cases=total_active_cases,
            date=district.date
        )
        return district_dto