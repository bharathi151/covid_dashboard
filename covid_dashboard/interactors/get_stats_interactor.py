from .storages.user_storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface

class MandalStatsInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_mandal_stats(self):
        stats_dto = self.storage.\
            get_mandal_stats_dto()
        response = self.presenter.get_mandal_stats_dto_response(
            stats_dto=stats_dto
        )
        return response
