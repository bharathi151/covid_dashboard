from .storages.state_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface
from .storages.dtos import (StateCumulativeDto, DistrictCumulativeDto,
                            StateCumulativeDtos
                            )

class StateCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_state_cumulative_details(self, till_date):
        cumulative_dto = self.storage.\
            get_state_cumulative_details_dto(till_date=till_date)
        total_active_cases = self._get_total_active_cases(
                cumulative_dto = cumulative_dto
            )
        state_dto = StateCumulativeDto(
            state_name=cumulative_dto.state_name,
            total_confirmed_cases=cumulative_dto.total_confirmed_cases,
            total_recovered_cases=cumulative_dto.total_recovered_cases,
            total_deaths=cumulative_dto.total_deaths,
            total_active_cases=total_active_cases
        )
        districts_dtos = self._get_districts_dtos(cumulative_dto=cumulative_dto)
        state_cumulative_dtos = StateCumulativeDtos(
            state=state_dto,
            districts=districts_dtos
            ) 
        response = self.presenter.get_state_cumulative_details_dto_response(
            state_cumulative_dto=state_cumulative_dtos
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
        districts_dtos = []
        for district in cumulative_dto.districts:
            total_active_cases = self._get_total_active_cases(district)
            districts_dtos.append(
                self._get_cumulative_district_dto(
                    district=district, total_active_cases=total_active_cases
                )
            )
        return districts_dtos


    def _get_cumulative_district_dto(self, district, total_active_cases):
        district_dto = DistrictCumulativeDto(
            district_name=district.district_name,
            district_id=district.district_id,
            total_confirmed_cases=district.total_confirmed_cases,
            total_recovered_cases=district.total_recovered_cases,
            total_deaths=district.total_deaths,
            total_active_cases=total_active_cases
        )
        return district_dto
