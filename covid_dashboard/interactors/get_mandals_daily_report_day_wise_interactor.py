from covid_dashboard.interactors.storages.storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface

from covid_dashboard.interactors.storages.dtos import *

class MandalsDailyDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_day_wise_mandals_daily_details(self, district_id, till_date):

        is_invalid_district_id = not self.storage.is_valid_district_id(
            district_id=district_id
        )
        if is_invalid_district_id:
            self.presenter.raise_invalid_district_id_exception()
            return

        mandals_daily_dtos = self.storage.\
            get_day_wise_mandals_daily_dto(district_id=district_id, till_date=till_date)
        response = self.presenter.get_day_wise_mandals_daily_details_dto_response(
            mandals_daily_dto=mandals_daily_dtos
        )
        return response