from .storages.user_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface

class InvalidMandalId(Exception):
    pass

class DataAlreadyExisted(Exception):
    pass

class PostCasesDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def post_cases_wrapper(self, 
                           presenter: PresenterInterface,
                           mandal_id: int,
                           date: str,
                           confirmed_cases:int,
                           recovered_cases:int,
                           deaths:int):
        self.presenter = presenter
        try:
           stats_dto = self.post_cases_details(
                mandal_id=mandal_id,
                date=date,
                confirmed_cases=confirmed_cases,
                deaths=deaths,
                recovered_cases=recovered_cases
            )
        except InvalidMandalId:
            return self.presenter.raise_invalid_mandal_id_exception()
        except DataAlreadyExisted:
            return self.presenter.raise_date_already_existed()
        return self.presenter.post_cases_details_response(
                stats_dto=stats_dto
            )

    def post_cases_details(self,
                           mandal_id: int,
                           date: str,
                           confirmed_cases:int,
                           recovered_cases:int,
                           deaths:int):

        is_invalid_mandal_id = not self.storage.is_valid_mandal_id(mandal_id=mandal_id)
        if is_invalid_mandal_id:
            raise InvalidMandalId
        is_mandal_data_for_date_already_existed = self.storage. \
                is_mandal_data_for_date_already_existed(date=date, mandal_id=mandal_id)
        if is_mandal_data_for_date_already_existed:
            raise DataAlreadyExisted

        stats_dto= self.storage.post_cases_details(
            mandal_id=mandal_id,
            date=date,
            confirmed_cases=confirmed_cases,
            deaths=deaths,
            recovered_cases=recovered_cases
        )

        return stats_dto

