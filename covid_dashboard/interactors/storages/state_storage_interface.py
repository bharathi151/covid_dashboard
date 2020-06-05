from abc import ABC
from abc import abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_state_cumulative_details_dto(self, till_date: date) -> StateTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_state_cumulative_dto(self) -> DayWiseStateTotalCasesDtos:
        pass

    @abstractmethod
    def get_day_wise_districts_cumulative_dto(self) -> DayWiseDistrictTotalCasesDtos:
        pass

    @abstractmethod
    def get_state_daily_details_dto(self, date: date) -> StateTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_state_daily_dto(self, till_date: str) -> DayWiseStateTotalCasesDtos:
        pass