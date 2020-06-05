from .storages.storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface


class DistrictDailyDetailsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_district_daily_details(self, till_date, district_id):
        daily_dto = self.storage.\
            get_district_daily_details_dto(date=till_date, district_id=district_id)
        response = self.presenter.get_district_daily_details_dto_response(
            district_daily_dto=daily_dto
        )
        return response
