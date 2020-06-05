from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class StateCumulativeDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_state_cumulative_details(self):
        cumulative_dto = self.storage.\
            get_day_wise_state_cumulative_dto()

        state_dtos = self._get_state_dtos(cumulative_dto=cumulative_dto)
        state_cumulative_dtos = DayWiseStateCumulativeDtos(
            state_name=cumulative_dto.state_name,
            day_wise_statistics=state_dtos
            ) 

        response = self.presenter.get_day_wise_state_cumulative_details_dto_response(
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
        return total_active_cases

    def _get_state_dtos(self, cumulative_dto):
        state_dtos = []
        for state in cumulative_dto.day_wise_statistics:
            total_active_cases = self._get_total_active_cases(state)
            state_dtos.append(
                self._get_day_wise_cumulative_state_dto(
                    state=state, total_active_cases=total_active_cases
                )
            )
        return state_dtos


    def _get_day_wise_cumulative_state_dto(self, state, total_active_cases):
        state_dto = DayWiseStateCumulativeDto(
            total_recovered_cases=state.total_recovered_cases,
            total_confirmed_cases=state.total_confirmed_cases,
            total_deaths=state.total_deaths,
            total_active_cases=total_active_cases,
            date=state.date
        )
        return state_dto