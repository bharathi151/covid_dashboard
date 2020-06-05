from .storages.state_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface

class StateDailyDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_state_daily_details(self, till_date):
        daily_dto = self.storage.\
            get_state_daily_details_dto(date=till_date)
        response = self.presenter.get_state_daily_details_dto_response(
            state_daily_dto=daily_dto
        )
        return response
