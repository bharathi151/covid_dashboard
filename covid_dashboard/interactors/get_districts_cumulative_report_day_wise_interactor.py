from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class DistrictsCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_districts_cumulative_details(self):

        cumulative_dto = self.storage.\
            get_day_wise_districts_cumulative_dto()
        districts_dtos = self._get_districts_dtos(cumulative_dto=cumulative_dto)
        districts_cumulative_dtos = DayWiseDistrictCumulativeDtos(
            districts=districts_dtos
            ) 
        response = self.presenter.get_day_wise_districts_cumulative_details_dto_response(
            districts_cumulative_dto=districts_cumulative_dtos
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

    def _get_districts_dtos(self, cumulative_dto):
        districts = []
        for district in cumulative_dto.districts:
            districts.append(
                self._get_district_dtos(district=district)
            )
        return districts

    def _get_district_dtos(self, district):
        day_wise_statistics = []
        for district_dto in district.day_wise_statistics:
            total_active_cases = self._get_total_active_cases(district_dto)
            day_wise_statistics.append(
                self._get_day_wise_cumulative_district_dto(
                    district=district_dto, total_active_cases=total_active_cases
                )
            )
        district_dtos = DayWiseDistrictCumulativeDto(
            district_name=district.district_name,
            district_id=district.district_id,
            day_wise_statistics=day_wise_statistics
        )
        return district_dtos


    def _get_day_wise_cumulative_district_dto(self, district, total_active_cases):
        state_dto = DayWiseCumulativeDto(
            total_recovered_cases=district.total_recovered_cases,
            total_confirmed_cases=district.total_confirmed_cases,
            total_deaths=district.total_deaths,
            total_active_cases=total_active_cases,
            date=district.date
        )
        return state_dto