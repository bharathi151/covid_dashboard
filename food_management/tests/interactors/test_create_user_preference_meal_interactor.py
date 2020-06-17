from unittest.mock import create_autospec
import pytest
import datetime
from food_management.interactors.storages.dtos import *
from food_management.interactors.create_user_meal import CreateUserPreferedmealInteractor
from food_management.interactors.presenters.presenter_interface import PresenterInterface
from food_management.interactors.storages.storage_interface import StorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_create_user_preference_meal_when_invalid_meal_given_raise_invalid_meal_id_exception():
    #arrange
    meal_id=1
    user_id=1
    items_quantities_dto=PreferedItemsQuantitiesDto(
        items_quantities=[
            ItemDto(item_id=1, quantity=2),
            ItemDto(item_id=2, quantity=1)
        ]
    )
    date_time=datetime.datetime.now()

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_meal_id.return_value = False
    presenter.raise_invalid_meal_id_exception.side_effect = NotFound
    interactor = CreateUserPreferedmealInteractor(
        storage = storage
    )
    #act
    with pytest.raises(NotFound):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter,
            meal_id=meal_id,
            datetime=date_time,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto)
    #assert
    storage.is_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    presenter.raise_invalid_meal_id_exception.assert_called_once()

def test_create_user_preference_meal_when_invalid_meal_items_given_raise_invalid_meal_items_exception():
    #arrange
    meal_id=1
    user_id=1
    items_quantities_dto=PreferedItemsQuantitiesDto(
        items_quantities=[
            ItemDto(item_id=1, quantity=2),
            ItemDto(item_id=2, quantity=1),
            ItemDto(item_id=4, quantity=1)
        ]
    )
    date_time=datetime.datetime.now()

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_meal_id.return_value = True
    storage.get_invalid_item_ids.return_value = []
    storage.get_meal_items_list.return_value = [1, 2, 3]
    presenter.raise_invalid_meal_items_exception.side_effect = BadRequest
    interactor = CreateUserPreferedmealInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter,
            meal_id=meal_id,
            datetime=date_time,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto)
    #assert
    storage.is_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    storage.get_meal_items_list.assert_called_once_with(
        meal_id=meal_id, datetime=date_time
    )
    presenter.raise_invalid_meal_items_exception.assert_called_once()
    call_args = presenter.raise_invalid_meal_items_exception.call_args
    call_obj = call_args.args
    error_obj = call_obj[0].invalid_items_ids
    assert error_obj == [4]

def test_create_user_preference_meal_when_duplicate_items_given_raise_duplicate_meal_items_exception():
    #arrange
    meal_id=1
    user_id=1
    items_quantities_dto=PreferedItemsQuantitiesDto(
        items_quantities=[
            ItemDto(item_id=1, quantity=2),
            ItemDto(item_id=2, quantity=1),
            ItemDto(item_id=1, quantity=1)
        ]
    )
    date_time=datetime.datetime.now()

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_meal_id.return_value = True
    storage.get_invalid_item_ids.return_value = []
    storage.get_meal_items_list.return_value = [1, 2, 3]
    presenter.raise_duplicate_meal_items_exception.side_effect = BadRequest
    interactor = CreateUserPreferedmealInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter,
            meal_id=meal_id,
            datetime=date_time,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto)
    #assert
    storage.is_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    storage.get_meal_items_list.assert_called_once_with(
        meal_id=meal_id, datetime=date_time
    )
    presenter.raise_duplicate_meal_items_exception.assert_called_once()
    call_args = presenter.raise_duplicate_meal_items_exception.call_args
    call_obj = call_args.args
    error_obj = call_obj[0].duplicate_items_ids
    assert error_obj == [1]

def test_create_user_preference_meal_when_negative_quantity_items_given_raise_negative_quantity_items_exception():
    #arrange
    meal_id=1
    user_id=1
    items_quantities_dto=PreferedItemsQuantitiesDto(
        items_quantities=[
            ItemDto(item_id=1, quantity=-2),
            ItemDto(item_id=2, quantity=1),
            ItemDto(item_id=3, quantity=1)
        ]
    )
    negative_quantities_items_dto = NegativeQuantityItemsDto(
        negative_quantities_items=[
            ItemDto(item_id=1, quantity=-2)
        ]
    )
    date_time=datetime.datetime.now()

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_meal_id.return_value = True
    storage.get_invalid_item_ids.return_value = []
    storage.get_meal_items_list.return_value = [1, 2, 3]
    presenter.raise_negative_quantity_items_exception.side_effect = BadRequest
    interactor = CreateUserPreferedmealInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter,
            meal_id=meal_id,
            datetime=date_time,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto)
    #assert
    storage.is_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    storage.get_meal_items_list.assert_called_once_with(
        meal_id=meal_id, datetime=date_time
    )
    presenter.raise_negative_quantity_items_exception.assert_called_once()
    call_args = presenter.raise_negative_quantity_items_exception.call_args
    call_obj = call_args.args
    print(call_obj)
    error_obj = call_obj[0].negative_quantities_items
    assert error_obj == negative_quantities_items_dto

def test_create_user_preference_meal_when_invalid_items_given_raise_invalid_items_exception():
    #arrange
    meal_id=1
    user_id=1
    items_quantities_dto=PreferedItemsQuantitiesDto(
        items_quantities=[
            ItemDto(item_id=1, quantity=2),
            ItemDto(item_id=2, quantity=1),
            ItemDto(item_id=4, quantity=1)
        ]
    )
    date_time=datetime.datetime.now()

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_meal_id.return_value = True
    storage.get_invalid_item_ids.return_value = [4]
    presenter.raise_invalid_items_exception.side_effect = NotFound
    interactor = CreateUserPreferedmealInteractor(
        storage = storage
    )
    #act
    with pytest.raises(NotFound):
        interactor.create_user_preference_meal_wrapper(
            presenter=presenter,
            meal_id=meal_id,
            datetime=date_time,
            user_id=user_id,
            items_quantities_dto=items_quantities_dto)
    #assert
    storage.is_valid_meal_id.assert_called_once_with(
        meal_id=meal_id
    )
    storage.get_invalid_item_ids.assert_called_once_with(
        items_quantities_dto = items_quantities_dto
    )
    presenter.raise_invalid_items_exception.assert_called_once()
    call_args = presenter.raise_invalid_items_exception.call_args
    call_obj = call_args.args
    error_obj = call_obj[0].invalid_items_ids
    assert error_obj == [4]
