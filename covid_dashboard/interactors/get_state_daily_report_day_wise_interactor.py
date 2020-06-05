from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class StateDailyDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_state_daily_details(self, till_date):

        daily_dto = self.storage.get_day_wise_state_daily_dto(
            till_date=till_date
        )


        response = self.presenter.get_day_wise_state_daily_details_dto_response(
            state_daily_dto=daily_dto
        )

        return response
