from abc import ABC
from abc import abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_state_cumulative_details_dto(self, till_date: str) -> StateTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_state_cumulative_dto(self, till_date: str) -> DayWiseStateTotalCasesDtos:
        pass
    

    # @abstractmethod
    # def add_day_data_to_state_report(
    #     self,
    #     state_name: str,
    #     district_name: str,
    #     confirmed_cases:int,
    #     recovered_cases_count:int,
    #     deaths_count:int
    # ) -> int:
    #     pass









