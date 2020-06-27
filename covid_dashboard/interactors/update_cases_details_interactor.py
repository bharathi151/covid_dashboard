from .storages.user_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface


class UpdateCasesDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

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
        is_mandal_data_for_date_already_existed = self.storage. \
                is_mandal_data_for_date_already_existed(date=date, mandal_id=mandal_id)

        is_invalid_cases_details = not self.storage. \
                is_valid_cases_details(
                    confirmed_cases=confirmed_cases,
                    recovered_cases=recovered_cases,
                    deaths=deaths)
        if is_invalid_cases_details:
            self.presenter.raise_invalid_cases_details()

        if is_mandal_data_for_date_already_existed:
            stats_dto = self.storage.update_cases_details(
                mandal_id=mandal_id,
                date=date,
                confirmed_cases=confirmed_cases,
                deaths=deaths,
                recovered_cases=recovered_cases
            )
        else:
            self.presenter.raise_stats_not_existed()
            return

        response = self.presenter.update_cases_details_response(
            stats_dto=stats_dto
        )
        return response
