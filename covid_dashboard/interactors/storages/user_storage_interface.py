from abc import ABC
from abc import abstractmethod
from typing import List
from covid_dashboard.interactors.storages.dtos import *
from common.dtos import UserAuthTokensDTO

class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, user_name: str) -> bool:
        pass

    @abstractmethod
    def validate_password(self, user_name: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_user_id(self, user_name: str, password: str) -> int:
        pass

    @abstractmethod
    def sign_up(self, user_name: str, password:str, confirm_password: str) -> int:
        pass

    @abstractmethod
    def post_cases_details(self,
                          cases_details_dto: CasesDetailsDto) -> PostCasesDetailsDto:
        pass

    @abstractmethod
    def is_valid_cases_details(self,
                                 confirmed_cases: int,
                                 recovered_cases: int,
                                 deaths: int):
        pass

    @abstractmethod
    def update_cases_details(self,
                           cases_details_dto: CasesDetailsDto) -> PostCasesDetailsDto:
        pass

    @abstractmethod
    def is_valid_mandal_id(self,  mandal_id: int) -> bool:
        pass

    @abstractmethod
    def is_mandal_data_for_date_already_existed(self, date: str, mandal_id: int) -> bool:
        pass

    @abstractmethod
    def get_mandal_stats_dto(self):
        pass