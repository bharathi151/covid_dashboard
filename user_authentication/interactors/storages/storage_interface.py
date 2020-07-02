from abc import abstractmethod
from typing import List

from user_authentication.interactors.storages.dtos import UserDTO


class StorageInterface:

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass
