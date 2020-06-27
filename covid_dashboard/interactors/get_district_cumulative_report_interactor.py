from .storages.storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface
from .storages.dtos import (DistrictCumulativeDto, MandalCumulativeDto,
                            DistrictCumulativeDtos
                            )

class DistrictCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_district_cumulative_details(self, till_date, district_id):
        is_invalid_district_id = not self.storage.is_valid_district_id(
            district_id=district_id
        )
        if is_invalid_district_id:
            self.presenter.raise_invalid_district_id_exception()
            return

        cumulative_dto = self.storage.get_district_cumulative_details_dto(
                till_date=till_date, district_id=district_id
            )
        total_active_cases = self._get_total_active_cases(
                cumulative_dto = cumulative_dto
            )
        district_dto = DistrictCumulativeDto(
            district_name=cumulative_dto.district_name,
            district_id=cumulative_dto.district_id,
            total_confirmed_cases=cumulative_dto.total_confirmed_cases,
            total_recovered_cases=cumulative_dto.total_recovered_cases,
            total_deaths=cumulative_dto.total_deaths,
            total_active_cases=total_active_cases
        )
        mandal_dtos = self._get_mandals_dtos(cumulative_dto=cumulative_dto)
        district_cumulative_dtos = DistrictCumulativeDtos(
            district=district_dto,
            mandals=mandal_dtos
            ) 
        response = self.presenter.get_district_cumulative_details_dto_response(
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
        invalid_active_cases = not (total_active_cases >= 0)
        if invalid_active_cases:
            total_active_cases = 0

        return total_active_cases

    def _get_mandals_dtos(self, cumulative_dto):
        mandals_dtos = []
        for mandal in cumulative_dto.mandals:
            total_active_cases = self._get_total_active_cases(mandal)
            mandals_dtos.append(
                self._get_cumulative_mandal_dto(
                    mandal=mandal, total_active_cases=total_active_cases
                )
            )
        return mandals_dtos


    def _get_cumulative_mandal_dto(self, mandal, total_active_cases):
        mandal_dto = MandalCumulativeDto(
            mandal_name=mandal.mandal_name,
            mandal_id=mandal.mandal_id,
            total_confirmed_cases=mandal.total_confirmed_cases,
            total_recovered_cases=mandal.total_recovered_cases,
            total_deaths=mandal.total_deaths,
            total_active_cases=total_active_cases
        )
        return mandal_dto
