from .storages.user_storage_interface import StorageInterface
from .presenters.presenter_interface import PostCasesPresenterInterface
from covid_dashboard.interactors.storages.dtos import *


class PostAndUpdateCasesDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PostCasesPresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_cases_details(self,
                           mandal_id: int,
                           date: str,
                           confirmed_cases:int,
                           recovered_cases:int,
                           deaths:int):

        is_invalid_mandal_id = not self.storage.is_valid_mandal_id(mandal_id=mandal_id)
        if is_invalid_mandal_id:
            self.presenter.raise_invalid_mandal_id_exception()
            return
        is_mandal_data_for_date_already_existed = self.storage. \
                is_mandal_data_for_date_already_existed(date=date, mandal_id=mandal_id)
        if is_mandal_data_for_date_already_existed:
            self.presenter.raise_date_already_existed()
            return

        is_invalid_cases_details = not self.storage. \
                is_valid_cases_details(
                    confirmed_cases=confirmed_cases,
                    recovered_cases=recovered_cases,
                    deaths=deaths)
        if is_invalid_cases_details:
            self.presenter.raise_invalid_cases_details()
            return

        cases_details_dto = CasesDetailsDto(
            mandal_id=mandal_id,
            date=date,
            confirmed_cases=confirmed_cases,
            recovered_cases=recovered_cases,
            deaths=deaths
        )
        stats_dto= self.storage.post_cases_details(
           cases_details_dto=cases_details_dto
        )

        response = self.presenter.post_cases_details_response(
            stats_dto=stats_dto
        )
        return response

    def update_cases_details(self,
                           mandal_id: int,
                           date: str,
                           confirmed_cases:int,
                           recovered_cases:int,
                           deaths:int):

        is_invalid_mandal_id = not self.storage.is_valid_mandal_id(mandal_id=mandal_id)
        if is_invalid_mandal_id:
            self.presenter.raise_invalid_mandal_id_exception()
            return
        is_mandal_data_for_date_not_existed = not self.storage. \
                is_mandal_data_for_date_already_existed(date=date, mandal_id=mandal_id)

        if is_mandal_data_for_date_not_existed:
            self.presenter.raise_stats_not_existed()
            return

        stats_dto = self.storage.update_cases_details(
            mandal_id=mandal_id,
            date=date,
            confirmed_cases=confirmed_cases,
            deaths=deaths,
            recovered_cases=recovered_cases
        )

        is_invalid_cases_details = not self.storage. \
                is_valid_cases_details(
                    confirmed_cases=confirmed_cases,
                    recovered_cases=recovered_cases,
                    deaths=deaths)
        if is_invalid_cases_details:
            self.presenter.raise_invalid_cases_details()
            return

        response = self.presenter.update_cases_details_response(
            stats_dto=stats_dto
        )
        return response
