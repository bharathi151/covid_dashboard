from .storages.state_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface

class DistrictZonesInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_districts_zones(self):
        zones_dto = self.storage.\
            get_districts_zones_dto()
        response = self.presenter.get_districts_zones_dto_response(
            zones_dto=zones_dto
        )
        return response
