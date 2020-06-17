from abc import ABC
from abc import abstractmethod
from typing import List
from food_management.interactors.storages.dtos import *

class StorageInterface(ABC):
    @abstractmethod
    def is_valid_meal_id(self, meal_id: int) -> bool:
        pass

    @abstractmethod
    def get_invalid_item_ids(
        self, items_quantities_dto: PreferedItemsQuantitiesDto
    ):
        pass

    @abstractmethod
    def is_meal_already_existed(self, datetime: str, user_id: int, meal_id: int) -> bool:
        pass

    @abstractmethod
    def create_user_preference_meal(self,
                           meal_id: int,
                           datetime: str,
                           user_id: int,
                           items_quantities_dto: PreferedItemsQuantitiesDto):
        pass

    @abstractmethod
    def update_user_preference_meal(self,
                           meal_id: int,
                           datetime: str,
                           user_id: int,
                           items_quantities_dto: PreferedItemsQuantitiesDto):
        pass

    @abstractmethod
    def get_meal_items_list(self, meal_id: int, datetime: str)-> PreferedItemsQuantitiesDto:
        pass
