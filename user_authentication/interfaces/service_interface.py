from typing import List

from user_authentication.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from user_authentication.storages.storage_implementation import StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = GetUserDetailsInteractor(storage=storage)
        user_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
