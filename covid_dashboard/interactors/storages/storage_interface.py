from abc import ABC
from abc import abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import *

class StorageInterface(ABC):
    @abstractmethod
    def is_valid_district_id(self, district_id: int) -> bool:
        pass

    @abstractmethod
    def get_district_cumulative_details_dto(self, till_date: date, district_id) -> DistrictTotalCasesDtos:
        pass

    @abstractmethod
    def get_day_wise_district_cumulative_dto(self, district_id: int) -> DayWiseDistrictTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_mandals_cumulative_dto(self, district_id: int) -> DayWiseMandalTotalCasesDtos:
        pass

    @abstractmethod
    def get_district_daily_details_dto(self, date: date, district_id: int) -> DistrictTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_district_daily_dto(self, district_id: int, till_date: str) -> DayWiseDistrictTotalCasesDto:
        pass

    @abstractmethod
    def get_day_wise_mandals_daily_dto(self, district_id: int, till_date:str) -> DayWiseMandalTotalCasesDtos:
        pass