from typing import List

from user_authentication.interactors.storages.storage_interface import \
    StorageInterface


class GetUserDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_details_wrapper(self, user_ids: List[int]):
        user_dtos = self.get_user_details_dtos(user_ids=user_ids)
        return user_dtos

    def get_user_details_dtos(self, user_ids: List[int]):
        user_dtos = self.storage.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
