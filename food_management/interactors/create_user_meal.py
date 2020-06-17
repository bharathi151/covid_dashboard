from typing import List
from .storages.storage_interface import StorageInterface
from .presenters.presenter_interface import PresenterInterface
from food_management.interactors.storages.dtos import *

class InvalidMealId(Exception):
    pass

class InvalidItems(Exception):
    def __init__(self, invalid_items_ids: List[int]):
        self.invalid_items_ids = invalid_items_ids

class InvalidMealItems(Exception):
    def __init__(self, invalid_items_ids: List[int]):
        self.invalid_items_ids = invalid_items_ids

class DuplicateMealItems(Exception):
    def __init__(self, duplicate_items_ids: List[int]):
        self.duplicate_items_ids = duplicate_items_ids

class NegativeQuantityItems(Exception):
    def __init__(self, negative_quantities_items: NegativeQuantityItemsDto):
        self.negative_quantities_items = negative_quantities_items

class CreateUserPreferedmealInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_user_preference_meal_wrapper(self, 
                           presenter: PresenterInterface,
                           meal_id: int,
                           user_id: int,
                           datetime: str,
                           items_quantities_dto: PreferedItemsQuantitiesDto):
        self.presenter = presenter
        try:
           person_meal_id = self.create_user_preference_meal(
                meal_id=meal_id,
                user_id=user_id,
                datetime=datetime,
                items_quantities_dto=items_quantities_dto
            )
        except InvalidMealId:
            return self.presenter.raise_invalid_meal_id_exception()
        except InvalidItems as error:
            return self.presenter.raise_invalid_items_exception(error)
        except InvalidMealItems as error:
            return self.presenter.raise_invalid_meal_items_exception(error)
        except DuplicateMealItems as error:
            return self.presenter.raise_duplicate_meal_items_exception(error)
        except NegativeQuantityItems as error:
            self.presenter.raise_negative_quantity_items_exception(error)

        return self.presenter.create_user_preference_meal_response(
                person_meal_id=person_meal_id
            )

    def create_user_preference_meal(self,
                           meal_id: int,
                           datetime: str,
                           user_id: int,
                           items_quantities_dto: PreferedItemsQuantitiesDto):

        is_invalid_meal_id = not self.storage.is_valid_meal_id(meal_id=meal_id)
        if is_invalid_meal_id:
            raise InvalidMealId

        invalid_items_ids = self.storage.get_invalid_item_ids(
            items_quantities_dto=items_quantities_dto
        )
        if invalid_items_ids:
            raise InvalidItems(invalid_items_ids=invalid_items_ids)

        meal_items = self.storage.get_meal_items_list(
            meal_id=meal_id,
            datetime=datetime)
        invalid_meal_items_ids = self.\
            _get_invalid_items_ids_in_user_prefered_items(
                items_quantities_dto=items_quantities_dto,
                meal_items=meal_items)
        if invalid_meal_items_ids:
            raise InvalidMealItems(invalid_items_ids=invalid_meal_items_ids)

        duplicate_items_ids = self.\
            _get_duplicate_items_ids_in_user_prefered_items(
                items_quantities_dto=items_quantities_dto)
        if duplicate_items_ids:
            raise DuplicateMealItems(duplicate_items_ids=duplicate_items_ids)

        negative_quantities_items = self.\
            _get_negative_quantity_items_in_user_prefered_items_dto(
                items_quantities_dto=items_quantities_dto)
        if negative_quantities_items:
            raise NegativeQuantityItems(negative_quantities_items=negative_quantities_items)

        is_user_meal_already_existed = self.storage. \
                is_meal_already_existed(datetime=datetime, meal_id=meal_id, user_id=user_id)
        if is_user_meal_already_existed:
            person_meal_id= self.storage.updatetime_user_preference_meal(
                meal_id=meal_id,
                datetime=datetime,
                user_id=user_id,
                items_quantities_dto=items_quantities_dto
            )
            return person_meal_id

        person_meal_id= self.storage.create_user_preference_meal(
            meal_id=meal_id,
            datetime=datetime,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto
        )

        return person_meal_id

    def _get_invalid_items_ids_in_user_prefered_items(
                self, items_quantities_dto, meal_items):
        invalid_items_ids = [item.item_id
             for item in items_quantities_dto.items_quantities
                if item.item_id not in meal_items
            ]
        return list(set(invalid_items_ids))

    def _get_duplicate_items_ids_in_user_prefered_items(
                self, items_quantities_dto):
        items_ids = [item.item_id
             for item in items_quantities_dto.items_quantities
             ]
        duplicate_items_ids = [item_id
            for item_id in items_ids
                if items_ids.count(item_id) > 1
            ]
        return list(set(duplicate_items_ids))

    def _get_negative_quantity_items_in_user_prefered_items_dto(
                self, items_quantities_dto):
        negative_quantities_items = []
        for item in items_quantities_dto.items_quantities:
            if item.quantity < 0:
                negative_quantities_items.append(
                    ItemDto(
                        item_id=item.item_id,
                        quantity=item.quantity
                    )
                )
        negative_quantities_items_dto = NegativeQuantityItemsDto(
            negative_quantities_items=negative_quantities_items 
        )
        return negative_quantities_items_dto
