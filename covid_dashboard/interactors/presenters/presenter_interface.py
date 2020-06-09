from abc import ABC
from abc import abstractmethod
from  typing import List
from common.dtos import UserAuthTokensDTO


from covid_dashboard.interactors.storages.dtos import *

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def get_log_in_user_response(self, tokens_dto: UserAuthTokensDTO):
        pass

    # @abstractmethod
    # def get_add_day_data_to_state_report_response(self, record_id: int):
    #     pass

    @abstractmethod
    def get_state_cumulative_details_dto_response(
        self, state_cumulative_dto: StateCumulativeDtos
    ):
        pass

    @abstractmethod
    def get_day_wise_state_cumulative_details_dto_response(
        self, state_cumulative_dto: DayWiseStateCumulativeDtos
    ):
        pass

    @abstractmethod
    def get_day_wise_districts_cumulative_details_dto_response(
        self, districts_cumulative_dto: DayWiseDistrictCumulativeDtos
    ):
        pass

    @abstractmethod
    def post_cases_details_response(self, stats_dto: CasesDetailsDto):
        pass

    @abstractmethod
    def update_cases_details_response(self, stats_dto: CasesDetailsDto):
        pass

    @abstractmethod
    def raise_invalid_mandal_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_district_id_exception(self):
        pass
    
    @abstractmethod
    def raise_date_already_existed(self):
        pass

    @abstractmethod
    def raise_stats_not_existed(self):
        pass

    @abstractmethod
    def get_district_cumulative_details_dto_response(
        self, district_cumulative_dto: DistrictCumulativeDtos
        ):
        pass

    @abstractmethod
    def get_day_wise_district_cumulative_details_dto_response(
            self, district_cumulative_dto: DayWiseDistrictCumulativeDto):
        pass

    @abstractmethod
    def get_day_wise_mandals_cumulative_details_dto_response(
        self, mandals_cumulative_dto: DayWiseMandalCumulativeDtos
        ):
        pass

    @abstractmethod
    def get_state_daily_details_dto_response(self, state_daily_dto: StateTotalCasesDto):
        pass

    @abstractmethod
    def get_district_daily_details_dto_response(self, district_daily_dto: DistrictTotalCasesDto):
        pass

    @abstractmethod
    def get_day_wise_district_daily_details_dto_response(
        self, district_daily_dto: DayWiseDistrictTotalCasesDto):
        pass

    @abstractmethod
    def get_day_wise_state_daily_details_dto_response(
        self, state_daily_dto: DayWiseStateTotalCasesDtos):
        pass
    @abstractmethod
    def get_day_wise_mandals_daily_details_dto_response(
            self, mandals_daily_dto: DayWiseMandalTotalCasesDtos):
        pass

    @abstractmethod
    def get_mandal_stats_dto_response(self, stats_dto):
        pass

    @abstractmethod
    def get_districts_zones_dto_response(
            self, zones_dto: DistrictZones):
        pass